import mdac.helpers.general_function as gf


class TestUnescape:

    def test_ref_ending(self):
        block = r'[@test\]\]]'
        exp_res = r'[@test]]]'
        assert gf.unescape_block(block) == exp_res

    def test_ref_beginning(self):
        block = r'\[@test]'
        exp_res = r'[@test]'
        assert gf.unescape_block(block) == exp_res
