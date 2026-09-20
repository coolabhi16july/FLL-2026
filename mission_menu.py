"""Mission selector built with the official Pybricks ``hub_menu`` helper.

See https://pybricks.com/project/spike-hub-menu/ for the reference
implementation this file follows.
"""


from pybricks.tools import hub_menu, wait

# Import mission modules
import m01_m02_surface_map as m01_m02
import m13_statuerebuild_deliver_artifact as m13
import m11_m12_angler_salvage as m11_m12
import m03_m13_m09_mineshaft_statue_market as m03_m13_m09
import m05_m06_m07_m08_habitat_forge_lift_silo as m05_m06_m07_m08
import m10_scales as m10

# Mission dictionary
OPTION_LABELS = ("1", "2", "3", "4", "5", "6")
MISSIONS = {
    "1": m01_m02.run_mission_1_2,
    "2": m13.run_mission_13,
    "3": m11_m12.run_mission_11_12,
    "4": m03_m13_m09.run_mission_3_13_9,
    "5": m05_m06_m07_m08.run_mission_5_6_7_8,
    "6": m10.run_mission_10,
}


while True:
    selection = hub_menu(*OPTION_LABELS)
    mission_callable = MISSIONS.get(selection)
    if mission_callable:
        try:
            mission_callable()
        except Exception as exc:
            print("[Menu] Mission error:", repr(exc))
    wait(500)