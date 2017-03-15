from src.models import code_model, constant_model, figure_model, \
    include_model, table_model, theorem_model
from unit_test.helpers.constants_for_test import *
from unit_test.helpers.functions_for_test import *


class TestLoadDict:
    ###################################
    #
    # Testing Code Model
    def test_code_model(self):
        model = code_model.CodeModel()
        model.load_dict(
            input_dict=code_test_dict_with_file
        )

        assert model.label == 'test_code'
        assert model.syntax == 'python'
        assert model.caption == 'this is a test code'
        assert model.file == './unit_test/resources/resource.py'

    def test_code_miss_para(self):
        model = code_model.CodeModel()

        miss_dict, miss_para = remove_one_para(
            para_dict=code_test_dict_with_file,
            require_para_list=code_req_para)
        try:
            model.load_dict(
                input_dict=miss_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() missing 1 required " \
                             "positional argument: '{0}'".format(miss_para)

    def test_code_more_para(self):
        model = code_model.CodeModel()
        extra_dict, extra_key = add_one_para(
            para_dict=code_test_dict_with_file,
            extra_para_list=other_para_list
        )

        try:
            model.load_dict(
                input_dict=extra_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() got an unexpected" \
                             " keyword argument '{0}'".format(extra_key)

    ###################################
    #
    # Testing Constant Model
    def test_constant_model(self):
        model = constant_model.ConstantModel()
        model.load_dict(
            input_dict=constant_test_dict
        )

        assert model.label == 'constant1'
        assert model.content == 'this is the test to replace it with'

    def test_constant_miss_para(self):
        model = constant_model.ConstantModel()

        miss_dict, miss_para = remove_one_para(
            para_dict=constant_test_dict,
            require_para_list=constant_req_para)
        try:
            model.load_dict(
                input_dict=miss_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() missing 1 required " \
                             "positional argument: '{0}'".format(miss_para)

    def test_constant_more_para(self):
        model = constant_model.ConstantModel()
        extra_dict, extra_key = add_one_para(
            para_dict=constant_test_dict,
            extra_para_list=other_para_list
        )

        try:
            model.load_dict(
                input_dict=extra_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() got an unexpected" \
                             " keyword argument '{0}'".format(extra_key)

    ###################################
    #
    # Testing Figure Model
    def test_figure_model(self):
        model = figure_model.FigureModel()
        model.load_dict(
            input_dict=figure_test_dict
        )

        assert model.label == 'fig:figid'
        assert model.source == './image/git.png'
        assert model.caption == 'this is a image'
        assert model.width == '30'
        assert model.height == '20'
        assert model.code == 'pass'

    def test_figure_miss_para(self):
        model = figure_model.FigureModel()
        miss_dict, miss_para = remove_one_para(
            para_dict=figure_test_dict,
            require_para_list=figure_req_para)
        try:
            model.load_dict(
                input_dict=miss_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() missing 1 required " \
                             "positional argument: '{0}'".format(miss_para)

    def test_figure_more_para(self):
        model = figure_model.FigureModel()
        extra_dict, extra_key = add_one_para(
            para_dict=figure_test_dict,
            extra_para_list=other_para_list
        )

        try:
            model.load_dict(
                input_dict=extra_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() got an unexpected" \
                             " keyword argument '{0}'".format(extra_key)

    ###################################
    #
    # Testing include Model
    def test_include_model(self):
        model = include_model.IncludeModel()
        model.load_dict(
            input_dict=include_test_dict
        )

        assert model.file == 'src/test.md'

    def test_include_miss_para(self):
        model = include_model.IncludeModel()

        miss_dict, miss_para = remove_one_para(
            para_dict=include_test_dict,
            require_para_list=include_req_para)
        try:
            model.load_dict(
                input_dict=miss_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() missing 1 required " \
                             "positional argument: '{0}'".format(miss_para)

    def test_include_more_para(self):
        model = include_model.IncludeModel()
        extra_dict, extra_key = add_one_para(
            para_dict=include_test_dict,
            extra_para_list=other_para_list
        )

        try:
            model.load_dict(
                input_dict=extra_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() got an unexpected" \
                             " keyword argument '{0}'".format(extra_key)

    ###################################
    #
    # Testing Table Model
    def test_table_model(self):
        model = table_model.TableModel()
        model.load_dict(
            input_dict=table_test_dict_with_file
        )

        assert model.file == './unit_test/resources/test.csv'
        assert model.top_header is True
        assert model.caption == 'this is a table'
        assert model.label == 'tbl: testTable'

    def test_table_miss_para(self):
        model = table_model.TableModel()

        miss_dict, miss_para = remove_one_para(
            para_dict=table_test_dict_with_file,
            require_para_list=table_req_para)
        try:
            model.load_dict(
                input_dict=miss_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() missing 1 required " \
                             "positional argument: '{0}'".format(miss_para)

    def test_table_more_para(self):
        model = table_model.TableModel()
        extra_dict, extra_key = add_one_para(
            para_dict=table_test_dict_with_file,
            extra_para_list=other_para_list
        )

        try:
            model.load_dict(
                input_dict=extra_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() got an unexpected" \
                             " keyword argument '{0}'".format(extra_key)

    ###################################
    #
    # Testing Table Model
    def test_theorem_model(self):
        model = theorem_model.TheoremModel()
        model.load_dict(
            input_dict=theorem_test_dict
        )

        assert model.label == 'thm:maxwell eq'
        assert model.content == 'great theorem'
        assert model.theorem_type == 'Lemma'

    def test_theorem_miss_para(self):
        model = theorem_model.TheoremModel()

        miss_dict, miss_para = remove_one_para(
            para_dict=theorem_test_dict,
            require_para_list=theorem_req_para)
        try:
            model.load_dict(
                input_dict=miss_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() missing 1 required " \
                             "positional argument: '{0}'".format(miss_para)

    def test_theorem_more_para(self):
        model = theorem_model.TheoremModel()
        extra_dict, extra_key = add_one_para(
            para_dict=theorem_test_dict,
            extra_para_list=other_para_list
        )

        try:
            model.load_dict(
                input_dict=extra_dict
            )
        except TypeError as e:
            assert str(e) == "__construct__() got an unexpected" \
                             " keyword argument '{0}'".format(extra_key)
