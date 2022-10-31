from lib.part.gate import Gate

def test_bipolar_transistor():
    part = Gate(kind="Bipolar", technology="Digital", nb_gates=10)
    assert part.C1C2() == {"C1": 0.0025, "C2": 0.0025}
    part.set_gates(100)
    assert part.C1C2() == {"C1": 0.0025, "C2": 0.0025}
    part.set_gates(101)
    assert part.C1C2() == {"C1": 0.005, "C2": 0.005}
    part.set_gates(1001)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part.set_gates(2999)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part.set_gates(3000)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part.set_gates(3001)
    assert part.C1C2() == {"C1": 0.02, "C2": 0.02}
    part.set_gates(10000)
    assert part.C1C2() == {"C1": 0.02, "C2": 0.02}
    part.set_gates(10001)
    assert part.C1C2() == {"C1": 0.04, "C2": 0.04}
    part.set_gates(30000)
    assert part.C1C2() == {"C1": 0.04, "C2": 0.04}
    part.set_gates(30001)
    assert part.C1C2() == {"C1": 0.08, "C2": 0.08}
    part.set_gates(60000)
    assert part.C1C2() == {"C1": 0.08, "C2": 0.08}
    part.set_gates(80000)
    assert part.C1C2() == {"C1": 0.08, "C2": 0.08}

    part.set_technology("Linear")
    part.set_gates(10)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part.set_gates(99)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part.set_gates(100)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part.set_gates(101)
    assert part.C1C2() == {"C1": 0.02, "C2": 0.02}
    part.set_gates(299)
    assert part.C1C2() == {"C1": 0.02, "C2": 0.02}
    part.set_gates(300)
    assert part.C1C2() == {"C1": 0.02, "C2": 0.02}
    part.set_gates(301)
    assert part.C1C2() == {"C1": 0.04, "C2": 0.04}
    part.set_gates(1000)
    assert part.C1C2() == {"C1": 0.04, "C2": 0.04}
    part.set_gates(10000)
    assert part.C1C2() == {"C1": 0.06, "C2": 0.06}
    part.set_gates(20000)
    assert part.C1C2() == {"C1": 0.06, "C2": 0.06}

    part.set_technology("PAL")
    part.set_gates(10)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}

def test_mos_transistor():
    part = Gate(kind="MOS", technology="Digital", nb_gates=10)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part = Gate(kind="MOS", technology="Linear", nb_gates=10)
    assert part.C1C2() == {"C1": 0.01, "C2": 0.01}
    part = Gate(kind="MOS", technology="PAL", nb_gates=10)
    assert part.C1C2() == {"C1": 0.00085, "C2": 0.00085}
