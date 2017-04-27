import parkingApp
import pytest

#@pytest.mark.skip(reason="This test fails")
def test_status():
	jmustatus = parkingApp.status("Resident")
	assert jmustatus == ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","R13","R14"]

#@pytest.mark.skip(reason="This test fails")
def test_whichStaff():
	whichJmuStaff = parkingApp.whichStaff("Red Zone")
	assert whichJmuStaff == ["1077 South Main Street", "131 West Grace Street", "A Lot", "B Lot", "C6 Lot SADAH", "Cantrell Ave Deck Level 2", "Cantrell Ave Deck Level 3", "Grace Street Deck Level 2", "Grace Street Deck Level 3", "Grace Street Deck Level 4", "Grace Street Deck Level 5", "Grace Street Deck Level 6", "Grace Street Deck Level 7", "I Lot", "Ice House Lot", "J lot", "K Lot", "M Lot", "Mason Street Deck Faculty/Staff", "Memorial Hall", "N3 Lot", "Q Lot East", "Q Lot North", "Q Lot West", "R8 Lot Faculty/Staff", "S Lot", "T Lot", "V Lot", "W Lot", "Warsaw Ave Deck Level 2 faculty/staff", "Warsaw Ave Deck Level G", "X Lot", "Y Lot", "Z Lot"]