from typing import Any
from PyUtils.MetaReader import read_metadata
from Campaigns.Utils import getMCCampaign

# filename = "/data/R21/DAOD_PHYS/361022/DAOD_EXOT15.26710681._000512.pool.root.1"

# filename = "/data/asg_test_data/100events_ttbar.FullSim.DAOD_PHYSLITE.pool.root"
# filename = "/data/asg_test_data/mc_410470_ttbar.DAOD_PHYS.22.2.110.pool.root.1"
# filename = "/data/asg_test_data/mc_311321_physVal_Main.21.2.143.pool.root"
filename = "/data/asg_test_data/mc20_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.22.2.113.pool.root"

md = read_metadata(filename, mode='lite')

assert len(md.keys()) == 1


def to_string(v) -> str:
    if isinstance(v, (str, int, float)):
        return str(v)
    if isinstance(v, list):
        add_on = ", ..." if len(v) > 5 else ""
        return '[' + ", ".join(to_string(item) for item in v[:5]) + add_on + ']'
    else:
        return str(type(v))


def print_simple(k: str, v: Any, indent: str = ""):
    print(f'{indent}{k}: {to_string(v)}')


file_md = list(md.values())[0]
for k, v in file_md.items():
    print_simple(k, v)
    # if k == "metadata_items":
    #     print(f'{k}:')
    #     for m_k, m_v in file_md.items():
    #         print_simple(m_k, m_v, '  ')            
    # else:
    #     print_simple(k, v)

print(f'MC Campaign: {getMCCampaign(filename)}')
