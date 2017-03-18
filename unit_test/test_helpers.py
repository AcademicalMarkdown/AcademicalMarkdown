import src.helpers.general_function as gf
from src.models.theorem_model import TheoremModel


class TestToKeywordPara:
    def test_dict(self):
        """
        test a dict input to return itself
        """
        test_instance = {"source": "this is a test",
                         "label": "label hahaha",
                         "file": "filename.py",
                         "header": True}
        assert gf.positional_to_keyword_para(
            model=TheoremModel,
            paras=test_instance
        ) == test_instance

    def test_pure_list(self):
        """
        test a list of dict, each dict has only one element
        """
        test_instance = [{"source": "this is a test"},
                         {"label": "label hahaha"},
                         {"file": "filename.py"},
                         {"header": True}]

        expect_res = {"source": "this is a test",
                      "label": "label hahaha",
                      "file": "filename.py",
                      "header": True}

        assert gf.positional_to_keyword_para(
            model=TheoremModel,
            paras=test_instance
        ) == expect_res

    def test_positional_with_pure_list(self):
        """
        test positional parameter mixed with dict in a list.
         each list has only one element.
        """
        test_instance = ["this is a test theorem",
                         {"label": "label hahaha"},
                         {"file": "filename.py"},
                         {"header": True}]

        expect_res = {"content": "this is a test theorem",
                      "label": "label hahaha",
                      "file": "filename.py",
                      "header": True}

        assert gf.positional_to_keyword_para(
            model=TheoremModel,
            paras=test_instance
        ) == expect_res

    def test_mix_dict_list(self):
        """
        test only dicts in the list,
        each dicts has different number of elements
        """
        test_instance = [{"content": "this is a test theorem"},
                         {"label": "label hahaha"},
                         {"file": "filename.py",
                          "header": True}]

        expect_res = {"content": "this is a test theorem",
                      "label": "label hahaha",
                      "file": "filename.py",
                      "header": True}

        assert gf.positional_to_keyword_para(
            model=TheoremModel,
            paras=test_instance
        ) == expect_res

    def test_positional_with_mixed(self):
        """
        test positional parameter followed by dicts in the list.
        each dicts contains different number of elements.
        """
        test_instance = ["this is a test theorem",
                         {"label": "label hahaha"},
                         {"file": "filename.py",
                          "header": True}]

        expect_res = {"content": "this is a test theorem",
                      "label": "label hahaha",
                      "file": "filename.py",
                      "header": True}

        assert gf.positional_to_keyword_para(
            model=TheoremModel,
            paras=test_instance
        ) == expect_res


class TestUnescape:
    def test_yaml(self):
        block = '\\%--- \\---%'
        exp_res = '%--- ---%'
        assert gf.unescape_block(block) == exp_res

    def test_yaml_unescape(self):
        block = r'\\%--- \\---%'
        exp_res = '\\%--- \\---%'
        assert gf.unescape_block(block) == exp_res

    def test_ref_ending(self):
        block = r'[@test\]\]]'
        exp_res = r'[@test]]]'
        assert gf.unescape_block(block) == exp_res

    def test_ref_beginning(self):
        block = r'\[@test]'
        exp_res = r'[@test]'
        assert gf.unescape_block(block) == exp_res
