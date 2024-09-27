# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computational_dp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63omputational_dp.proto\x12\x11smiles.model.comp\x1a\x1cgoogle/protobuf/struct.proto\"\x9f\t\n\x0f\x43omputationalDP\x12\x17\n\x0f\x64\x61ta_product_id\x18\x01 \x01(\t\x12#\n\x16parent_data_product_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ndye_family\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tstructure\x18\x05 \x01(\x0cH\x03\x88\x01\x01\x12\x13\n\x0bother_names\x18\x06 \x03(\t\x12\x11\n\x04note\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x19\n\x0cproject_name\x18\x08 \x01(\tH\x05\x88\x01\x01\x12\x1c\n\x0f\x65xperiment_name\x18\t \x01(\tH\x06\x88\x01\x01\x12\x15\n\x08username\x18\n \x01(\tH\x07\x88\x01\x01\x12\x19\n\x0cindexed_time\x18\x0b \x01(\x03H\x08\x88\x01\x01\x12K\n\x15\x65xecution_environment\x18\x0c \x01(\x0b\x32\'.smiles.model.comp.ExecutionEnvironmentH\t\x88\x01\x01\x12K\n\x15\x63\x61lculated_properties\x18\r \x01(\x0b\x32\'.smiles.model.comp.CalculatedPropertiesH\n\x88\x01\x01\x12\x61\n!final_molecule_structural_formats\x18\x0e \x01(\x0b\x32\x31.smiles.model.comp.FinalMoleculeStructuralFormatsH\x0b\x88\x01\x01\x12\x32\n\x08molecule\x18\x0f \x01(\x0b\x32\x1b.smiles.model.comp.MoleculeH\x0c\x88\x01\x01\x12\x38\n\x0b\x63\x61lculation\x18\x10 \x01(\x0b\x32\x1e.smiles.model.comp.CalculationH\r\x88\x01\x01\x12\x38\n\x0bidentifiers\x18\x11 \x01(\x0b\x32\x1e.smiles.model.comp.IdentifiersH\x0e\x88\x01\x01\x12,\n\x05\x66iles\x18\x12 \x01(\x0b\x32\x18.smiles.model.comp.FilesH\x0f\x88\x01\x01\x12P\n\x18input_file_configuration\x18\x13 \x01(\x0b\x32).smiles.model.comp.InputFileConfigurationH\x10\x88\x01\x01\x12\x17\n\x0frelated_records\x18\x14 \x03(\tB\x19\n\x17_parent_data_product_idB\x07\n\x05_nameB\r\n\x0b_dye_familyB\x0c\n\n_structureB\x07\n\x05_noteB\x0f\n\r_project_nameB\x12\n\x10_experiment_nameB\x0b\n\t_usernameB\x0f\n\r_indexed_timeB\x18\n\x16_execution_environmentB\x18\n\x16_calculated_propertiesB$\n\"_final_molecule_structural_formatsB\x0b\n\t_moleculeB\x0e\n\x0c_calculationB\x0e\n\x0c_identifiersB\x08\n\x06_filesB\x1b\n\x19_input_file_configuration\"\xee\x02\n\x14\x45xecutionEnvironment\x12\x14\n\x07\x63\x61lc_by\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0fjob_cpu_runtime\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x19\n\x0c\x63\x61lc_machine\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1f\n\x12\x61\x63tual_job_runtime\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x15\n\x08\x66in_time\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06memory\x18\x06 \x01(\x05H\x05\x88\x01\x01\x12\x1a\n\rn_proc_shared\x18\x07 \x01(\x05H\x06\x88\x01\x01\x12\x1a\n\rfin_timestamp\x18\x08 \x01(\x03H\x07\x88\x01\x01\x42\n\n\x08_calc_byB\x12\n\x10_job_cpu_runtimeB\x0f\n\r_calc_machineB\x15\n\x13_actual_job_runtimeB\x0b\n\t_fin_timeB\t\n\x07_memoryB\x10\n\x0e_n_proc_sharedB\x10\n\x0e_fin_timestamp\"\xc4\x0b\n\x14\x43\x61lculatedProperties\x12\x12\n\x05homos\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06\x65nergy\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12.\n\x06\x64ipole\x18\x03 \x01(\x0b\x32\x19.smiles.model.comp.DipoleH\x02\x88\x01\x01\x12\x0f\n\x02hf\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12)\n\x1dmaximum_gradient_distribution\x18\x05 \x03(\x01\x42\x02\x10\x01\x12%\n\x19rms_gradient_distribution\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x16\n\niterations\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x1d\n\x10homo_eigen_value\x18\x08 \x01(\x01H\x04\x88\x01\x01\x12\x19\n\x11homo_eigen_values\x18\t \x03(\t\x12\x1d\n\x10lumo_eigen_value\x18\n \x01(\x01H\x05\x88\x01\x01\x12\x19\n\x11lumo_eigen_values\x18\x0b \x03(\t\x12\x14\n\x07thermal\x18\x0c \x01(\x01H\x06\x88\x01\x01\x12\x15\n\x08\x65nthalpy\x18\r \x01(\x01H\x07\x88\x01\x01\x12\x12\n\x05gibbs\x18\x0e \x01(\x01H\x08\x88\x01\x01\x12\x1f\n\x13\x65nergy_distribution\x18\x0f \x03(\x01\x42\x02\x10\x01\x12\x13\n\x06n_imag\x18\x10 \x01(\x05H\t\x88\x01\x01\x12\x1e\n\x11zero_point_energy\x18\x11 \x01(\x01H\n\x88\x01\x01\x12\x42\n\x1b\x65xperimental_absorption_max\x18\x12 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x0b\x88\x01\x01\x12@\n\x19\x65xperimental_emission_max\x18\x13 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x0c\x88\x01\x01\x12\x36\n\x0fimom_absorption\x18\x14 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\r\x88\x01\x01\x12\x39\n\x12sc_imom_absorption\x18\x15 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x0e\x88\x01\x01\x12\x37\n\x10sc_imom_emission\x18\x16 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x0f\x88\x01\x01\x12\x37\n\x10tddft_absorption\x18\x17 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x10\x88\x01\x01\x12:\n\x13tddft_absorption_s2\x18\x18 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x11\x88\x01\x01\x12\x35\n\x0etddft_emission\x18\x19 \x01(\x0b\x32\x18.smiles.model.comp.ValueH\x12\x88\x01\x01\x12;\n\rea_quantities\x18\x1a \x01(\x0b\x32\x1f.smiles.model.comp.EAQuantitiesH\x13\x88\x01\x01\x12;\n\rip_quantities\x18\x1b \x01(\x0b\x32\x1f.smiles.model.comp.IPQuantitiesH\x14\x88\x01\x01\x42\x08\n\x06_homosB\t\n\x07_energyB\t\n\x07_dipoleB\x05\n\x03_hfB\x13\n\x11_homo_eigen_valueB\x13\n\x11_lumo_eigen_valueB\n\n\x08_thermalB\x0b\n\t_enthalpyB\x08\n\x06_gibbsB\t\n\x07_n_imagB\x14\n\x12_zero_point_energyB\x1e\n\x1c_experimental_absorption_maxB\x1c\n\x1a_experimental_emission_maxB\x12\n\x10_imom_absorptionB\x15\n\x13_sc_imom_absorptionB\x13\n\x11_sc_imom_emissionB\x13\n\x11_tddft_absorptionB\x16\n\x14_tddft_absorption_s2B\x11\n\x0f_tddft_emissionB\x10\n\x0e_ea_quantitiesB\x10\n\x0e_ip_quantities\"\xb2\x01\n\x1e\x46inalMoleculeStructuralFormats\x12\x10\n\x03sdf\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03pdb\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03xyz\x18\x03 \x01(\x0cH\x02\x88\x01\x01\x12\x42\n\x14optimized_geometries\x18\x04 \x03(\x0b\x32$.smiles.model.comp.OptimizedGeometryB\x06\n\x04_sdfB\x06\n\x04_pdbB\x06\n\x04_xyz\"\xde\x01\n\x08Molecule\x12\x14\n\x07\x66ormula\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06n_atom\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x0cmultiplicity\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x13\n\x06\x63harge\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x14\n\x07orb_sym\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08\x65lec_sym\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\n\n\x08_formulaB\t\n\x07_n_atomB\x0f\n\r_multiplicityB\t\n\x07_chargeB\n\n\x08_orb_symB\x0b\n\t_elec_sym\"\xdf\x02\n\x0b\x43\x61lculation\x12\x17\n\njob_status\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x62\x61sis\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03nmo\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x15\n\x08keywords\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07n_basis\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x30\n\x0bmo_energies\x18\x06 \x01(\x0b\x32\x16.google.protobuf.ValueH\x05\x88\x01\x01\x12\x14\n\x07package\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x16\n\tcalc_type\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x14\n\x07methods\x18\t \x01(\tH\x08\x88\x01\x01\x42\r\n\x0b_job_statusB\x08\n\x06_basisB\x06\n\x04_nmoB\x0b\n\t_keywordsB\n\n\x08_n_basisB\x0e\n\x0c_mo_energiesB\n\n\x08_packageB\x0c\n\n_calc_typeB\n\n\x08_methods\"\xa5\x01\n\x0bIdentifiers\x12\x16\n\tinchi_key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10\x63\x61nonical_smiles\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05inchi\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06smiles\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x0c\n\n_inchi_keyB\x13\n\x11_canonical_smilesB\x08\n\x06_inchiB\t\n\x07_smiles\"\xcb\x03\n\x05\x46iles\x12\x18\n\x0bsmiles_file\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1f\n\x12sdf_structure_file\x18\x02 \x01(\tH\x01\x88\x01\x01\x12!\n\x14gaussian_output_file\x18\x03 \x01(\tH\x02\x88\x01\x01\x12 \n\x13gaussian_input_file\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1f\n\x12pdb_structure_file\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x17\n\ninchi_file\x18\x06 \x01(\tH\x05\x88\x01\x01\x12%\n\x18gaussian_checkpoint_file\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\'\n\x1agaussian_f_checkpoint_file\x18\x08 \x01(\tH\x07\x88\x01\x01\x42\x0e\n\x0c_smiles_fileB\x15\n\x13_sdf_structure_fileB\x17\n\x15_gaussian_output_fileB\x16\n\x14_gaussian_input_fileB\x15\n\x13_pdb_structure_fileB\r\n\x0b_inchi_fileB\x1b\n\x19_gaussian_checkpoint_fileB\x1d\n\x1b_gaussian_f_checkpoint_file\"z\n\x16InputFileConfiguration\x12\x1c\n\x0flink_0_commands\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0eroute_commands\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x12\n\x10_link_0_commandsB\x11\n\x0f_route_commands\")\n\x06\x44ipole\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"$\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x0c\n\x04unit\x18\x02 \x01(\t\"\xce\x01\n\x0c\x45\x41Quantities\x12!\n\x14\x65lectron_affinity_ev\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12(\n\x1b\x61\x64iabatic_electron_affinity\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12 \n\x13reduction_potential\x18\x03 \x01(\x01H\x02\x88\x01\x01\x42\x17\n\x15_electron_affinity_evB\x1e\n\x1c_adiabatic_electron_affinityB\x16\n\x14_reduction_potential\"\xb0\x01\n\x0cIPQuantities\x12!\n\x14ionization_potential\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x19\n\x0c\x61\x64iabatic_ip\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12 \n\x13oxidation_potential\x18\x03 \x01(\x01H\x02\x88\x01\x01\x42\x17\n\x15_ionization_potentialB\x0f\n\r_adiabatic_ipB\x16\n\x14_oxidation_potential\".\n\x11OptimizedGeometry\x12\x0b\n\x03xyz\x18\x01 \x01(\x0c\x12\x0c\n\x04type\x18\x02 \x01(\tb\x06proto3')



_COMPUTATIONALDP = DESCRIPTOR.message_types_by_name['ComputationalDP']
_EXECUTIONENVIRONMENT = DESCRIPTOR.message_types_by_name['ExecutionEnvironment']
_CALCULATEDPROPERTIES = DESCRIPTOR.message_types_by_name['CalculatedProperties']
_FINALMOLECULESTRUCTURALFORMATS = DESCRIPTOR.message_types_by_name['FinalMoleculeStructuralFormats']
_MOLECULE = DESCRIPTOR.message_types_by_name['Molecule']
_CALCULATION = DESCRIPTOR.message_types_by_name['Calculation']
_IDENTIFIERS = DESCRIPTOR.message_types_by_name['Identifiers']
_FILES = DESCRIPTOR.message_types_by_name['Files']
_INPUTFILECONFIGURATION = DESCRIPTOR.message_types_by_name['InputFileConfiguration']
_DIPOLE = DESCRIPTOR.message_types_by_name['Dipole']
_VALUE = DESCRIPTOR.message_types_by_name['Value']
_EAQUANTITIES = DESCRIPTOR.message_types_by_name['EAQuantities']
_IPQUANTITIES = DESCRIPTOR.message_types_by_name['IPQuantities']
_OPTIMIZEDGEOMETRY = DESCRIPTOR.message_types_by_name['OptimizedGeometry']
ComputationalDP = _reflection.GeneratedProtocolMessageType('ComputationalDP', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTATIONALDP,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.ComputationalDP)
  })
_sym_db.RegisterMessage(ComputationalDP)

ExecutionEnvironment = _reflection.GeneratedProtocolMessageType('ExecutionEnvironment', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONENVIRONMENT,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.ExecutionEnvironment)
  })
_sym_db.RegisterMessage(ExecutionEnvironment)

CalculatedProperties = _reflection.GeneratedProtocolMessageType('CalculatedProperties', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATEDPROPERTIES,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.CalculatedProperties)
  })
_sym_db.RegisterMessage(CalculatedProperties)

FinalMoleculeStructuralFormats = _reflection.GeneratedProtocolMessageType('FinalMoleculeStructuralFormats', (_message.Message,), {
  'DESCRIPTOR' : _FINALMOLECULESTRUCTURALFORMATS,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.FinalMoleculeStructuralFormats)
  })
_sym_db.RegisterMessage(FinalMoleculeStructuralFormats)

Molecule = _reflection.GeneratedProtocolMessageType('Molecule', (_message.Message,), {
  'DESCRIPTOR' : _MOLECULE,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.Molecule)
  })
_sym_db.RegisterMessage(Molecule)

Calculation = _reflection.GeneratedProtocolMessageType('Calculation', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATION,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.Calculation)
  })
_sym_db.RegisterMessage(Calculation)

Identifiers = _reflection.GeneratedProtocolMessageType('Identifiers', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIERS,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.Identifiers)
  })
_sym_db.RegisterMessage(Identifiers)

Files = _reflection.GeneratedProtocolMessageType('Files', (_message.Message,), {
  'DESCRIPTOR' : _FILES,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.Files)
  })
_sym_db.RegisterMessage(Files)

InputFileConfiguration = _reflection.GeneratedProtocolMessageType('InputFileConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _INPUTFILECONFIGURATION,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.InputFileConfiguration)
  })
_sym_db.RegisterMessage(InputFileConfiguration)

Dipole = _reflection.GeneratedProtocolMessageType('Dipole', (_message.Message,), {
  'DESCRIPTOR' : _DIPOLE,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.Dipole)
  })
_sym_db.RegisterMessage(Dipole)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.Value)
  })
_sym_db.RegisterMessage(Value)

EAQuantities = _reflection.GeneratedProtocolMessageType('EAQuantities', (_message.Message,), {
  'DESCRIPTOR' : _EAQUANTITIES,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.EAQuantities)
  })
_sym_db.RegisterMessage(EAQuantities)

IPQuantities = _reflection.GeneratedProtocolMessageType('IPQuantities', (_message.Message,), {
  'DESCRIPTOR' : _IPQUANTITIES,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.IPQuantities)
  })
_sym_db.RegisterMessage(IPQuantities)

OptimizedGeometry = _reflection.GeneratedProtocolMessageType('OptimizedGeometry', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZEDGEOMETRY,
  '__module__' : 'computational_dp_pb2'
  # @@protoc_insertion_point(class_scope:smiles.model.comp.OptimizedGeometry)
  })
_sym_db.RegisterMessage(OptimizedGeometry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CALCULATEDPROPERTIES.fields_by_name['maximum_gradient_distribution']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['maximum_gradient_distribution']._serialized_options = b'\020\001'
  _CALCULATEDPROPERTIES.fields_by_name['rms_gradient_distribution']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['rms_gradient_distribution']._serialized_options = b'\020\001'
  _CALCULATEDPROPERTIES.fields_by_name['iterations']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['iterations']._serialized_options = b'\020\001'
  _CALCULATEDPROPERTIES.fields_by_name['energy_distribution']._options = None
  _CALCULATEDPROPERTIES.fields_by_name['energy_distribution']._serialized_options = b'\020\001'
  _COMPUTATIONALDP._serialized_start=76
  _COMPUTATIONALDP._serialized_end=1259
  _EXECUTIONENVIRONMENT._serialized_start=1262
  _EXECUTIONENVIRONMENT._serialized_end=1628
  _CALCULATEDPROPERTIES._serialized_start=1631
  _CALCULATEDPROPERTIES._serialized_end=3107
  _FINALMOLECULESTRUCTURALFORMATS._serialized_start=3110
  _FINALMOLECULESTRUCTURALFORMATS._serialized_end=3288
  _MOLECULE._serialized_start=3291
  _MOLECULE._serialized_end=3513
  _CALCULATION._serialized_start=3516
  _CALCULATION._serialized_end=3867
  _IDENTIFIERS._serialized_start=3870
  _IDENTIFIERS._serialized_end=4035
  _FILES._serialized_start=4038
  _FILES._serialized_end=4497
  _INPUTFILECONFIGURATION._serialized_start=4499
  _INPUTFILECONFIGURATION._serialized_end=4621
  _DIPOLE._serialized_start=4623
  _DIPOLE._serialized_end=4664
  _VALUE._serialized_start=4666
  _VALUE._serialized_end=4702
  _EAQUANTITIES._serialized_start=4705
  _EAQUANTITIES._serialized_end=4911
  _IPQUANTITIES._serialized_start=4914
  _IPQUANTITIES._serialized_end=5090
  _OPTIMIZEDGEOMETRY._serialized_start=5092
  _OPTIMIZEDGEOMETRY._serialized_end=5138
# @@protoc_insertion_point(module_scope)
