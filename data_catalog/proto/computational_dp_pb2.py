# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computational_dp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63omputational_dp.proto\x12\x0csmiles.model\x1a\x1cgoogle/protobuf/struct.proto\"\xe3\x07\n\x0f\x43omputationalDP\x12\x17\n\x0f\x64\x61ta_product_id\x18\x01 \x01(\t\x12#\n\x16parent_data_product_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bProjectName\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1b\n\x0e\x45xperimentName\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08Username\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x0f\n\x02Id\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x18\n\x0bIndexedTime\x18\x08 \x01(\x03H\x06\x88\x01\x01\x12\x45\n\x14\x45xecutionEnvironment\x18\t \x01(\x0b\x32\".smiles.model.ExecutionEnvironmentH\x07\x88\x01\x01\x12\x45\n\x14\x43\x61lculatedProperties\x18\n \x01(\x0b\x32\".smiles.model.CalculatedPropertiesH\x08\x88\x01\x01\x12Y\n\x1e\x46inalMoleculeStructuralFormats\x18\x0b \x01(\x0b\x32,.smiles.model.FinalMoleculeStructuralFormatsH\t\x88\x01\x01\x12-\n\x08Molecule\x18\x0c \x01(\x0b\x32\x16.smiles.model.MoleculeH\n\x88\x01\x01\x12\x33\n\x0b\x43\x61lculation\x18\r \x01(\x0b\x32\x19.smiles.model.CalculationH\x0b\x88\x01\x01\x12\x33\n\x0bIdentifiers\x18\x0e \x01(\x0b\x32\x19.smiles.model.IdentifiersH\x0c\x88\x01\x01\x12\'\n\x05\x46iles\x18\x0f \x01(\x0b\x32\x13.smiles.model.FilesH\r\x88\x01\x01\x12I\n\x16InputFileConfiguration\x18\x10 \x01(\x0b\x32$.smiles.model.InputFileConfigurationH\x0e\x88\x01\x01\x42\x19\n\x17_parent_data_product_idB\x07\n\x05_nameB\x0e\n\x0c_ProjectNameB\x11\n\x0f_ExperimentNameB\x0b\n\t_UsernameB\x05\n\x03_IdB\x0e\n\x0c_IndexedTimeB\x17\n\x15_ExecutionEnvironmentB\x17\n\x15_CalculatedPropertiesB!\n\x1f_FinalMoleculeStructuralFormatsB\x0b\n\t_MoleculeB\x0e\n\x0c_CalculationB\x0e\n\x0c_IdentifiersB\x08\n\x06_FilesB\x19\n\x17_InputFileConfiguration\"\xda\x02\n\x14\x45xecutionEnvironment\x12\x13\n\x06\x43\x61lcBy\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rJobCPURunTime\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x18\n\x0b\x43\x61lcMachine\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10\x41\x63tualJobRunTime\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x14\n\x07\x46inTime\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06Memory\x18\x06 \x01(\x05H\x05\x88\x01\x01\x12\x18\n\x0bNProcShared\x18\x07 \x01(\x05H\x06\x88\x01\x01\x12\x19\n\x0c\x46inTimeStamp\x18\x08 \x01(\x03H\x07\x88\x01\x01\x42\t\n\x07_CalcByB\x10\n\x0e_JobCPURunTimeB\x0e\n\x0c_CalcMachineB\x13\n\x11_ActualJobRunTimeB\n\n\x08_FinTimeB\t\n\x07_MemoryB\x0e\n\x0c_NProcSharedB\x0f\n\r_FinTimeStamp\"\xee\x04\n\x14\x43\x61lculatedProperties\x12\x12\n\x05Homos\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06\x45nergy\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12)\n\x06\x44ipole\x18\x03 \x01(\x0b\x32\x14.smiles.model.DipoleH\x02\x88\x01\x01\x12\x0f\n\x02HF\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\'\n\x1bMaximumGradientDistribution\x18\x05 \x03(\x01\x42\x02\x10\x01\x12#\n\x17RMSGradientDistribution\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x16\n\nIterations\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x1b\n\x0eHomoEigenvalue\x18\x08 \x01(\x01H\x04\x88\x01\x01\x12\x17\n\x0fHomoEigenvalues\x18\t \x03(\t\x12\x1b\n\x0eLumoEigenvalue\x18\n \x01(\x01H\x05\x88\x01\x01\x12\x17\n\x0fLumoEigenvalues\x18\x0b \x03(\t\x12\x14\n\x07Thermal\x18\x0c \x01(\x01H\x06\x88\x01\x01\x12\x15\n\x08\x45nthalpy\x18\r \x01(\x01H\x07\x88\x01\x01\x12\x12\n\x05Gibbs\x18\x0e \x01(\x01H\x08\x88\x01\x01\x12\x1e\n\x12\x45nergyDistribution\x18\x0f \x03(\x01\x42\x02\x10\x01\x12\x12\n\x05NImag\x18\x10 \x01(\x05H\t\x88\x01\x01\x12\x1c\n\x0fZeroPointEnergy\x18\x11 \x01(\x01H\n\x88\x01\x01\x42\x08\n\x06_HomosB\t\n\x07_EnergyB\t\n\x07_DipoleB\x05\n\x03_HFB\x11\n\x0f_HomoEigenvalueB\x11\n\x0f_LumoEigenvalueB\n\n\x08_ThermalB\x0b\n\t_EnthalpyB\x08\n\x06_GibbsB\x08\n\x06_NImagB\x12\n\x10_ZeroPointEnergy\"T\n\x1e\x46inalMoleculeStructuralFormats\x12\x10\n\x03SDF\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03PDB\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_SDFB\x06\n\x04_PDB\"\xd8\x01\n\x08Molecule\x12\x14\n\x07\x46ormula\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05NAtom\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x0cMultiplicity\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x13\n\x06\x43harge\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x13\n\x06OrbSym\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07\x45lecSym\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\n\n\x08_FormulaB\x08\n\x06_NAtomB\x0f\n\r_MultiplicityB\t\n\x07_ChargeB\t\n\x07_OrbSymB\n\n\x08_ElecSym\"\xd7\x02\n\x0b\x43\x61lculation\x12\x16\n\tJobStatus\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x42\x61sis\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03NMO\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x15\n\x08Keywords\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x13\n\x06NBasis\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12/\n\nMoEnergies\x18\x06 \x01(\x0b\x32\x16.google.protobuf.ValueH\x05\x88\x01\x01\x12\x14\n\x07Package\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x15\n\x08\x43\x61lcType\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x14\n\x07Methods\x18\t \x01(\tH\x08\x88\x01\x01\x42\x0c\n\n_JobStatusB\x08\n\x06_BasisB\x06\n\x04_NMOB\x0b\n\t_KeywordsB\t\n\x07_NBasisB\r\n\x0b_MoEnergiesB\n\n\x08_PackageB\x0b\n\t_CalcTypeB\n\n\x08_Methods\"\xa1\x01\n\x0bIdentifiers\x12\x15\n\x08InChIKey\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0f\x43\x61nonicalSMILES\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05InChI\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06SMILES\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x0b\n\t_InChIKeyB\x12\n\x10_CanonicalSMILESB\x08\n\x06_InChIB\t\n\x07_SMILES\"\xad\x03\n\x05\x46iles\x12\x17\n\nSMILESFile\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10SDFStructureFile\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x12GaussianOutputFile\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1e\n\x11GaussianInputFile\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1d\n\x10PDBStructureFile\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x16\n\tInChIFile\x18\x06 \x01(\tH\x05\x88\x01\x01\x12#\n\x16GaussianCheckpointFile\x18\x07 \x01(\tH\x06\x88\x01\x01\x12$\n\x17GaussianFCheckpointFile\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\r\n\x0b_SMILESFileB\x13\n\x11_SDFStructureFileB\x15\n\x13_GaussianOutputFileB\x14\n\x12_GaussianInputFileB\x13\n\x11_PDBStructureFileB\x0c\n\n_InChIFileB\x19\n\x17_GaussianCheckpointFileB\x1a\n\x18_GaussianFCheckpointFile\"t\n\x16InputFileConfiguration\x12\x1a\n\rLink0Commands\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rRouteCommands\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_Link0CommandsB\x10\n\x0e_RouteCommands\")\n\x06\x44ipole\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'computational_dp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CALCULATEDPROPERTIES.fields_by_name['MaximumGradientDistribution']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['MaximumGradientDistribution']._serialized_options = b'\020\001'
  _CALCULATEDPROPERTIES.fields_by_name['RMSGradientDistribution']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['RMSGradientDistribution']._serialized_options = b'\020\001'
  _CALCULATEDPROPERTIES.fields_by_name['Iterations']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['Iterations']._serialized_options = b'\020\001'
  _CALCULATEDPROPERTIES.fields_by_name['EnergyDistribution']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['EnergyDistribution']._serialized_options = b'\020\001'
  _COMPUTATIONALDP._serialized_start=71
  _COMPUTATIONALDP._serialized_end=1066
  _EXECUTIONENVIRONMENT._serialized_start=1069
  _EXECUTIONENVIRONMENT._serialized_end=1415
  _CALCULATEDPROPERTIES._serialized_start=1418
  _CALCULATEDPROPERTIES._serialized_end=2040
  _FINALMOLECULESTRUCTURALFORMATS._serialized_start=2042
  _FINALMOLECULESTRUCTURALFORMATS._serialized_end=2126
  _MOLECULE._serialized_start=2129
  _MOLECULE._serialized_end=2345
  _CALCULATION._serialized_start=2348
  _CALCULATION._serialized_end=2691
  _IDENTIFIERS._serialized_start=2694
  _IDENTIFIERS._serialized_end=2855
  _FILES._serialized_start=2858
  _FILES._serialized_end=3287
  _INPUTFILECONFIGURATION._serialized_start=3289
  _INPUTFILECONFIGURATION._serialized_end=3405
  _DIPOLE._serialized_start=3407
  _DIPOLE._serialized_end=3448
# @@protoc_insertion_point(module_scope)
