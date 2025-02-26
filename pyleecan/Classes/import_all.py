# -*- coding: utf-8 -*-

"""File generated by generate_code() - 
WARNING! All changes made in this file will be lost!
"""

from ..Classes.Arc import Arc
from ..Classes.Arc1 import Arc1
from ..Classes.Arc2 import Arc2
from ..Classes.Arc3 import Arc3
from ..Classes.Bore import Bore
from ..Classes.BoreFlower import BoreFlower
from ..Classes.BoreLSRPM import BoreLSRPM
from ..Classes.BoreUD import BoreUD
from ..Classes.CellMat import CellMat
from ..Classes.Circle import Circle
from ..Classes.CondType11 import CondType11
from ..Classes.CondType12 import CondType12
from ..Classes.CondType13 import CondType13
from ..Classes.CondType21 import CondType21
from ..Classes.CondType22 import CondType22
from ..Classes.Conductor import Conductor
from ..Classes.DXFImport import DXFImport
from ..Classes.DataKeeper import DataKeeper
from ..Classes.Drive import Drive
from ..Classes.DriveWave import DriveWave
from ..Classes.EEC import EEC
from ..Classes.EEC_LSRPM import EEC_LSRPM
from ..Classes.EEC_PMSM import EEC_PMSM
from ..Classes.EEC_SCIM import EEC_SCIM
from ..Classes.ElecLUTdq import ElecLUTdq
from ..Classes.Electrical import Electrical
from ..Classes.Elmer import Elmer
from ..Classes.ElmerResults import ElmerResults
from ..Classes.ElmerResultsVTU import ElmerResultsVTU
from ..Classes.EndWinding import EndWinding
from ..Classes.EndWindingCirc import EndWindingCirc
from ..Classes.EndWindingRect import EndWindingRect
from ..Classes.FPGNSeg import FPGNSeg
from ..Classes.FPGNTri import FPGNTri
from ..Classes.Force import Force
from ..Classes.ForceMT import ForceMT
from ..Classes.ForceTensor import ForceTensor
from ..Classes.Frame import Frame
from ..Classes.FrameBar import FrameBar
from ..Classes.GUIOption import GUIOption
from ..Classes.GaussPoint import GaussPoint
from ..Classes.Hole import Hole
from ..Classes.HoleM50 import HoleM50
from ..Classes.HoleM51 import HoleM51
from ..Classes.HoleM52 import HoleM52
from ..Classes.HoleM53 import HoleM53
from ..Classes.HoleM54 import HoleM54
from ..Classes.HoleM57 import HoleM57
from ..Classes.HoleM58 import HoleM58
from ..Classes.HoleMLSRPM import HoleMLSRPM
from ..Classes.HoleMag import HoleMag
from ..Classes.HoleUD import HoleUD
from ..Classes.Import import Import
from ..Classes.ImportData import ImportData
from ..Classes.ImportGenMatrixSin import ImportGenMatrixSin
from ..Classes.ImportGenPWM import ImportGenPWM
from ..Classes.ImportGenToothSaw import ImportGenToothSaw
from ..Classes.ImportGenVectLin import ImportGenVectLin
from ..Classes.ImportGenVectSin import ImportGenVectSin
from ..Classes.ImportMatlab import ImportMatlab
from ..Classes.ImportMatrix import ImportMatrix
from ..Classes.ImportMatrixVal import ImportMatrixVal
from ..Classes.ImportMatrixXls import ImportMatrixXls
from ..Classes.ImportMeshMat import ImportMeshMat
from ..Classes.ImportMeshUnv import ImportMeshUnv
from ..Classes.ImportVectorField import ImportVectorField
from ..Classes.Input import Input
from ..Classes.InputCurrent import InputCurrent
from ..Classes.InputFlux import InputFlux
from ..Classes.InputForce import InputForce
from ..Classes.InputVoltage import InputVoltage
from ..Classes.Interpolation import Interpolation
from ..Classes.LUT import LUT
from ..Classes.LUTdq import LUTdq
from ..Classes.LUTslip import LUTslip
from ..Classes.LamH import LamH
from ..Classes.LamHole import LamHole
from ..Classes.LamHoleNS import LamHoleNS
from ..Classes.LamSlot import LamSlot
from ..Classes.LamSlotMag import LamSlotMag
from ..Classes.LamSlotMulti import LamSlotMulti
from ..Classes.LamSlotMultiWind import LamSlotMultiWind
from ..Classes.LamSlotWind import LamSlotWind
from ..Classes.LamSquirrelCage import LamSquirrelCage
from ..Classes.LamSquirrelCageMag import LamSquirrelCageMag
from ..Classes.Lamination import Lamination
from ..Classes.Line import Line
from ..Classes.Loss import Loss
from ..Classes.LossFEMM import LossFEMM
from ..Classes.LossModel import LossModel
from ..Classes.LossModelBertotti import LossModelBertotti
from ..Classes.LossModelSteinmetz import LossModelSteinmetz
from ..Classes.LossModelWinding import LossModelWinding
from ..Classes.Machine import Machine
from ..Classes.MachineAsync import MachineAsync
from ..Classes.MachineDFIM import MachineDFIM
from ..Classes.MachineIPMSM import MachineIPMSM
from ..Classes.MachineLSPM import MachineLSPM
from ..Classes.MachineSCIM import MachineSCIM
from ..Classes.MachineSIPMSM import MachineSIPMSM
from ..Classes.MachineSRM import MachineSRM
from ..Classes.MachineSyRM import MachineSyRM
from ..Classes.MachineSync import MachineSync
from ..Classes.MachineUD import MachineUD
from ..Classes.MachineWRSM import MachineWRSM
from ..Classes.MagElmer import MagElmer
from ..Classes.MagFEMM import MagFEMM
from ..Classes.Magnet import Magnet
from ..Classes.Magnetics import Magnetics
from ..Classes.MatEconomical import MatEconomical
from ..Classes.MatElectrical import MatElectrical
from ..Classes.MatHT import MatHT
from ..Classes.MatMagnetics import MatMagnetics
from ..Classes.MatStructural import MatStructural
from ..Classes.Material import Material
from ..Classes.Mesh import Mesh
from ..Classes.MeshMat import MeshMat
from ..Classes.MeshSolution import MeshSolution
from ..Classes.MeshVTK import MeshVTK
from ..Classes.Mode import Mode
from ..Classes.ModelBH import ModelBH
from ..Classes.ModelBH_Langevin import ModelBH_Langevin
from ..Classes.ModelBH_arctangent import ModelBH_arctangent
from ..Classes.ModelBH_exponential import ModelBH_exponential
from ..Classes.ModelBH_linear_sat import ModelBH_linear_sat
from ..Classes.NodeMat import NodeMat
from ..Classes.Notch import Notch
from ..Classes.NotchEvenDist import NotchEvenDist
from ..Classes.OP import OP
from ..Classes.OPMatrix import OPMatrix
from ..Classes.OPdq import OPdq
from ..Classes.OPdqf import OPdqf
from ..Classes.OPslip import OPslip
from ..Classes.OptiBayesAlg import OptiBayesAlg
from ..Classes.OptiBayesAlgSmoot import OptiBayesAlgSmoot
from ..Classes.OptiConstraint import OptiConstraint
from ..Classes.OptiDesignVar import OptiDesignVar
from ..Classes.OptiGenAlg import OptiGenAlg
from ..Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap
from ..Classes.OptiObjective import OptiObjective
from ..Classes.OptiProblem import OptiProblem
from ..Classes.OptiSolver import OptiSolver
from ..Classes.OutElec import OutElec
from ..Classes.OutForce import OutForce
from ..Classes.OutGeo import OutGeo
from ..Classes.OutGeoLam import OutGeoLam
from ..Classes.OutInternal import OutInternal
from ..Classes.OutLoss import OutLoss
from ..Classes.OutMag import OutMag
from ..Classes.OutMagElmer import OutMagElmer
from ..Classes.OutMagFEMM import OutMagFEMM
from ..Classes.OutPost import OutPost
from ..Classes.OutStruct import OutStruct
from ..Classes.Output import Output
from ..Classes.ParamExplorer import ParamExplorer
from ..Classes.ParamExplorerInterval import ParamExplorerInterval
from ..Classes.ParamExplorerSet import ParamExplorerSet
from ..Classes.PolarArc import PolarArc
from ..Classes.Post import Post
from ..Classes.PostFunction import PostFunction
from ..Classes.PostLUT import PostLUT
from ..Classes.PostMethod import PostMethod
from ..Classes.PostPlot import PostPlot
from ..Classes.RefCell import RefCell
from ..Classes.RefLine3 import RefLine3
from ..Classes.RefQuad4 import RefQuad4
from ..Classes.RefQuad9 import RefQuad9
from ..Classes.RefSegmentP1 import RefSegmentP1
from ..Classes.RefTriangle3 import RefTriangle3
from ..Classes.RefTriangle6 import RefTriangle6
from ..Classes.ScalarProduct import ScalarProduct
from ..Classes.ScalarProductL2 import ScalarProductL2
from ..Classes.Section import Section
from ..Classes.Segment import Segment
from ..Classes.Shaft import Shaft
from ..Classes.Simu1 import Simu1
from ..Classes.Simulation import Simulation
from ..Classes.Skew import Skew
from ..Classes.SliceModel import SliceModel
from ..Classes.Slot import Slot
from ..Classes.Slot19 import Slot19
from ..Classes.SlotCirc import SlotCirc
from ..Classes.SlotDC import SlotDC
from ..Classes.SlotM10 import SlotM10
from ..Classes.SlotM11 import SlotM11
from ..Classes.SlotM12 import SlotM12
from ..Classes.SlotM13 import SlotM13
from ..Classes.SlotM14 import SlotM14
from ..Classes.SlotM15 import SlotM15
from ..Classes.SlotM16 import SlotM16
from ..Classes.SlotM17 import SlotM17
from ..Classes.SlotM18 import SlotM18
from ..Classes.SlotUD import SlotUD
from ..Classes.SlotUD2 import SlotUD2
from ..Classes.SlotW10 import SlotW10
from ..Classes.SlotW11 import SlotW11
from ..Classes.SlotW12 import SlotW12
from ..Classes.SlotW13 import SlotW13
from ..Classes.SlotW14 import SlotW14
from ..Classes.SlotW15 import SlotW15
from ..Classes.SlotW16 import SlotW16
from ..Classes.SlotW21 import SlotW21
from ..Classes.SlotW22 import SlotW22
from ..Classes.SlotW23 import SlotW23
from ..Classes.SlotW24 import SlotW24
from ..Classes.SlotW25 import SlotW25
from ..Classes.SlotW26 import SlotW26
from ..Classes.SlotW27 import SlotW27
from ..Classes.SlotW28 import SlotW28
from ..Classes.SlotW29 import SlotW29
from ..Classes.SlotW60 import SlotW60
from ..Classes.SlotW61 import SlotW61
from ..Classes.SlotWLSRPM import SlotWLSRPM
from ..Classes.Solution import Solution
from ..Classes.SolutionData import SolutionData
from ..Classes.SolutionMat import SolutionMat
from ..Classes.SolutionVector import SolutionVector
from ..Classes.SolverInputFile import SolverInputFile
from ..Classes.StructElmer import StructElmer
from ..Classes.Structural import Structural
from ..Classes.SurfLine import SurfLine
from ..Classes.SurfRing import SurfRing
from ..Classes.Surface import Surface
from ..Classes.Trapeze import Trapeze
from ..Classes.Unit import Unit
from ..Classes.VarLoad import VarLoad
from ..Classes.VarLoadCurrent import VarLoadCurrent
from ..Classes.VarLoadVoltage import VarLoadVoltage
from ..Classes.VarParam import VarParam
from ..Classes.VarSimu import VarSimu
from ..Classes.VentilationCirc import VentilationCirc
from ..Classes.VentilationPolar import VentilationPolar
from ..Classes.VentilationTrap import VentilationTrap
from ..Classes.Winding import Winding
from ..Classes.WindingSC import WindingSC
from ..Classes.WindingUD import WindingUD
from ..Classes.XOutput import XOutput
