"""Tests for DataBlock parser — basic construction and data access."""
from dae.parse.datablock import DataBlock, SharedDataBlock


class TestDataBlockBasic:
    def test_construct(self):
        blk = DataBlock(nameId=1, paramsCount=2, blocksCount=0, firstBlockId=0, ofs=0)
        assert blk.getNameId() == 1
        assert blk.getParamsCount() == 2
        assert blk.getblocksCount() == 0

    def test_properties(self):
        blk = DataBlock(nameId=5, paramsCount=3, blocksCount=1, firstBlockId=10, ofs=100)
        assert blk.getNameId() == 5
        assert blk.getParamsCount() == 3
        assert blk.getblocksCount() == 1
        assert blk.getFirstBlockId() == 10
        assert blk.getOfs() == 100

    def test_add_children(self):
        parent = DataBlock(nameId=0, paramsCount=0, blocksCount=2, firstBlockId=0, ofs=0)
        child1 = DataBlock(nameId=1, paramsCount=0, blocksCount=0, firstBlockId=0, ofs=10)
        child2 = DataBlock(nameId=2, paramsCount=0, blocksCount=0, firstBlockId=0, ofs=20)
        parent.addDataBlock(child1)
        parent.addDataBlock(child2)
        assert len(parent.getChildren()) == 2
        assert parent.getBlock(0).getNameId() == 1
        assert parent.getBlock(1).getNameId() == 2
        assert parent.getIsFull()


class TestSharedDataBlock:
    def test_get_block_name(self):
        nameMap = ["root", "child1", "child2"]
        shared = SharedDataBlock(1, nameMap, b"", None)  # blocksCount=1 via int arg
        assert shared.getBlockName(0) == "root"
        assert shared.getBlockName(1) == "child1"

    def test_get_by_name(self):
        nameMap = ["alpha", "beta"]
        shared = SharedDataBlock(2, nameMap, b"", None)
        # add a child block with matching name
        child = DataBlock(nameId=2, paramsCount=0, blocksCount=0, firstBlockId=0, ofs=0)
        child.setSharedBlk(shared)
        shared.addDataBlock(child)
        result = shared.getByName("beta")
        assert result.getNameId() == 2
