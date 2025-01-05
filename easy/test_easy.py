from easy.arrayHashing import TopKFrequent


def test_topKFrequent():
    assert set(TopKFrequent().topKFrequent([1,1,1,2,2,3], 2)) == {1, 2}

