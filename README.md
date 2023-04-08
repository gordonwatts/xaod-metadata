xaid-metadata

Quickly dump in-file metadata in an AnalysisRelease

## Introduction

There is currently no way to read in-file metadata in AnalysisBase. This code provides an example. This could provide the code
that does the work to be integrated into another tool that is distributed with AnalysisBase.

## Sample output

This is from running in AnalysisBase container 22.2.113, on a PHYSLITE file that is the ASG test file for that release.

```bash
[bash][atlas AnalysisBase-22.2.113]:xaod-metadata > python dump-metadata.py 
xAOD::Init                INFO    Environment initialised for data access
Py:MetaReader        INFO Current mode used: lite
Py:MetaReader        INFO Current filenames: ['/data/asg_test_data/mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.22.2.113.pool.root']
Py:MetaReader        INFO MetaReader is called with the parameter "unique_tag_info_values" set to True. This is a workaround to remove all duplicate values from "/TagInfo" key
Py:AutoConfigFlags    INFO Obtaining metadata of auto-configuration by peeking into '/data/asg_test_data/mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.22.2.113.pool.root'
Py:MetaReader        INFO Current mode used: lite
Py:MetaReader        INFO Current filenames: ['/data/asg_test_data/mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.22.2.113.pool.root']
Py:MetaReader        INFO MetaReader is called with the parameter "unique_tag_info_values" set to True. This is a workaround to remove all duplicate values from "/TagInfo" key
Py:AutoConfigFlags    INFO Looking into the file in 'peeker' mode as the configuration requires more details: mc_campaign 
Py:MetaReader        INFO Current mode used: peeker
Py:MetaReader        INFO Current filenames: ['/data/asg_test_data/mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.22.2.113.pool.root']
Py:MetaReader        INFO MetaReader is called with the parameter "unique_tag_info_values" set to True. This is a workaround to remove all duplicate values from "/TagInfo" key
file_type: POOL
file_size: 2570767
nentries: 100
auto_flush: 1000
file_guid: AF852C0F-63D4-2043-8285-7F4E3914FD71
file_comp_alg: 5
file_comp_level: 5
metadata_items: <class 'dict'>
beam_type: collisions
runNumbers: [310000]
mc_channel_number: 410470
lumiBlockNumbers: [8, 12, 14, 19, 20, ...]
beam_energy: 6500000.0
GeoAtlas: ATLAS-R2-2016-01-00-01
eventTypes: [IS_SIMULATION, IS_ATLAS]
processingTags: [StreamDAOD_PHYSLITE]
itemList: [<class 'tuple'>, <class 'tuple'>, <class 'tuple'>, <class 'tuple'>, <class 'tuple'>, ...]
**mc_campaign: Campaign.MC20e
```