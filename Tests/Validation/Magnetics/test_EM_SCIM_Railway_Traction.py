from os.path import join, isfile

import pytest

import numpy as np
from numpy.testing import assert_almost_equal

from SciDataTool.Functions.Plot.plot_2D import plot_2D

from pyleecan.Classes.OPslip import OPslip
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.LUTslip import LUTslip
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.VarLoadVoltage import VarLoadVoltage
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.MagFEMM import MagFEMM


from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import TEST_DIR, DATA_DIR

is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.SCIM
@pytest.mark.MagPMMF
@pytest.mark.MagFEMM
@pytest.mark.ImportMatlab
def test_EM_Railway_Traction_maxwell_current_enforced():
    """Validation of pmmf / linear femm for Railway_Traction machine with current enforced and
    comparison with Maxwell linear transient"""

    # Prepare simulation
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))
    Railway_Traction.stator.winding.Ntcoil = 21
    # Railway_Traction.plot()

    matlab_path = TEST_DIR + "/Data/Maxwell_Railway_Traction.mat"

    assert isfile(matlab_path)

    param_dict = dict()
    param_list = [
        "Emf_m",
        "Ibar_m_alpha",
        "Ibar_m_t",
        "jalpha0_m",
        "jt0_m",
        "nbar_m",
        "Tem_m",
        "XBr_m_alpha",
        "XBr_m_t",
        "XBt_m_alpha",
        "XBt_m_t",
    ]

    for param in param_list:
        value = ImportMatlab(file_path=matlab_path, var_name=param).get_data()
        if value.size == 1:
            if value.dtype == complex:
                param_dict[param] = complex(value)
            else:
                param_dict[param] = float(value)
        else:
            param_dict[param] = value

    # Convert Matlab index to python index
    jt0_m = [int(param_dict["jt0_m"] - 1)]

    simu = Simu1(
        name="test_EM_Railway_Traction_maxwell_current_enforced",
        machine=Railway_Traction,
    )

    simu.input = InputCurrent(
        OP=OPslip(I0_ref=40, IPhi0_ref=0, N0=1080, slip_ref=0.1),
        Na_tot=2000,
        Nt_tot=1,
        is_periodicity_a=True,
        is_periodicity_t=False,
        rot_dir=1,
        phase_dir=1,
        time=np.array([9.9980e-05]),
        Ir=param_dict["Ibar_m_alpha"],  # enforce rotor currents from Maxwell simulation
    )
    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=1,
        type_BH_rotor=2,
        type_BH_stator=2,
    )

    out = simu.run()

    B_maxwell = out.mag.B.copy()
    B_maxwell.components["radial"].values = param_dict["XBr_m_alpha"][None, :-1, None]
    B_maxwell.components["tangential"].values = param_dict["XBt_m_alpha"][
        None, :-1, None
    ]

    assert_almost_equal(out.mag.Tem.values - param_dict["Tem_m"][jt0_m], -2, decimal=0)
    assert_almost_equal(
        B_maxwell.components["radial"].values,
        out.mag.B.components["radial"].values,
        decimal=0,
    )

    assert_almost_equal(
        B_maxwell.components["tangential"].values,
        out.mag.B.components["tangential"].values,
        decimal=1,
    )

    if is_show_fig:
        B_maxwell.plot_2D_Data(
            "angle[smallestperiod]",
            "time[0]",
            component_list=["radial"],
            data_list=[out.mag.B],
            legend_list=["Maxwell", "FEMM"],
            linestyles=["solid", "dashed", "dotted"],
            **dict_2D,
        )

        B_maxwell.plot_2D_Data(
            "angle[smallestperiod]",
            "time[0]",
            component_list=["tangential"],
            data_list=[out.mag.B],
            legend_list=["Maxwell", "FEMM"],
            linestyles=["solid", "dashed"],
            **dict_2D,
        )

    return out


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.SCIM
@pytest.mark.MagFEMM
def test_EM_Railway_Traction_varslip():
    """Validation of pmmf / linear femm for Railway_Traction machine
    with current calculated with fundamental EEC"""

    # Prepare simulation
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))
    Railway_Traction.stator.winding.Ntcoil = 21
    # Railway_Traction.plot()

    simu = Simu1(name="test_EM_Railway_Traction_varslip", machine=Railway_Traction)

    U0_ref = 100
    N0 = 1080

    simu.input = InputVoltage(
        OP=OPslip(U0_ref=U0_ref, UPhi0_ref=0, N0=N0, slip_ref=0),
        Na_tot=500 * 4,
        Nt_tot=4 * 4,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    Nspeed = 10
    OP_matrix = np.zeros((Nspeed, 3))
    OP_matrix[:, 0] = N0
    OP_matrix[:, 1] = U0_ref
    OP_matrix[:, 2] = np.linspace(0, 0.1, Nspeed)

    simu.var_simu = VarLoadVoltage(is_keep_all_output=True)
    simu.var_simu.set_OP_array(
        OP_matrix, "N0", "U0", "slip", input_index=0, is_update_input=True
    )

    # Set values from Manatee V1
    Im = np.linspace(0, 200, 2)
    Lm = 0.0774 * np.ones(2)
    ELUT_Railway_Traction = LUTslip()
    ELUT_Railway_Traction.simu = Simu1(machine=Railway_Traction)
    ELUT_Railway_Traction.simu.elec = Electrical(
        eec=EEC_SCIM(
            R1=5.73,
            L1=0,
            Tsta=20,
            R2=0.1677,
            L2=0.0109,
            Trot=20,
            Lm_table=Lm,
            Im_table=Im,
            type_skin_effect=0,
        )
    )

    # Configure simulation
    simu.elec = Electrical(Tsta=20, Trot=20, LUT_enforced=ELUT_Railway_Traction)

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=4,
        type_BH_rotor=2,
        type_BH_stator=2,
    )

    # Run simulation
    out = simu.run()

    Tem_eec = np.array([out_ii.elec.Tem_av for out_ii in out.output_list])
    Tem_fem = np.array([out_ii.mag.Tem_av for out_ii in out.output_list])

    assert_almost_equal(Tem_eec, 1.05 * Tem_fem, decimal=0)

    if is_show_fig:
        plot_2D(
            [[out_ii.elec.OP.slip_ref for out_ii in out.output_list]],
            [Tem_eec, Tem_fem],
            xlabel="Mechanical slip",
            ylabel="Average torque [Nm]",
            legend_list=["EEC", "FEMM"],
        )

    return out


if __name__ == "__main__":

    # out = test_EM_Railway_Traction_maxwell_current_enforced()
    out = test_EM_Railway_Traction_varslip()
