"""Mission selector built with the official Pybricks ``hub_menu`` helper.

See https://pybricks.com/project/spike-hub-menu/ for the reference
implementation this file follows.
"""

from pybricks.tools import hub_menu, wait

# Import mission modules 
import m01_Drone_Survey as m01
import m03_m02_flip_the_rock_exploding_seeds as m03_m02
import m04_lucky_leaves as m04
import m06_m07_m011_final as m06_m07_11
import m09_lifting_the_platform as m09
import m12_forest_elder as m12
import m12_part2 as m12_2
import m13_keystone_species as m13


def main():
    """Main function to run the mission menu."""
    while True:
        selection = hub_menu("1", "2", "3", "4", "5", "6", "7", "8")
        if selection == "1":
            m01.run_mission_01()
        elif selection == "2":
            m03_m02.run_mission_03_02()
        elif selection == "3":
            m04.run_mission_04()
        elif selection == "4":
            m12_2.run_mission_12_2()
        elif selection == "5":
            m06_m07_11.run_mission_06_07_11()
        elif selection == "6":
            m09.run_mission_09()
        elif selection == "7":
            m12.run_mission_12()
        elif selection == "8":
            m13.run_mission_13()
        else:
            print("[Menu] Invalid selection:", selection)

if __name__ == "__main__":
    main()
