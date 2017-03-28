import yaml

from src.compilers.common_compilers.constants_compiler import const_compile
from src.compilers.common_compilers.header_compiler import HeaderCompiler
from src.registers.common_register import CommonRegister
from unit_test.helpers.constants_for_test import test_yaml_with_minus_ending, \
    test_yaml_with_output_conf
from unit_test.helpers.functions_for_test import list_eq_unorder


class TestHeaderCompiler:
    def test_minus_ending(self):
        CommonRegister.__clear__()

        compiler = HeaderCompiler()
        compiler.load_header(
            header_yaml=test_yaml_with_minus_ending
        )

        exp_const = {('test', 'test1'), ('test1', 'test 2')}
        exp_output_conf = []
        assert CommonRegister.get_constants_set() == exp_const
        assert CommonRegister.get_output_configs() == exp_output_conf

        exp_compil_res = '''
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
tags: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
...'''

        assert yaml.safe_load(compiler.compile()) == yaml.safe_load(
            exp_compil_res)

    def test_output_config(self):
        CommonRegister.__clear__()

        compiler = HeaderCompiler()
        compiler.load_header(
            header_yaml=test_yaml_with_output_conf
        )

        exp_const = set()
        exp_output_conf = [{'format': 'latex', 'default': True},
                           {'format': 'HTML', 'default': True}]
        assert CommonRegister.get_constants_set() == exp_const
        assert list_eq_unorder(CommonRegister.get_output_configs(),
                               exp_output_conf)

        exp_compil_res = '''
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
tags: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
...'''

        assert yaml.safe_load(compiler.compile()) == yaml.safe_load(
            exp_compil_res)

    class TestConstants:
        def test_constants(self):
            CommonRegister.__clear__()
            CommonRegister.register_constants([('test', 'test\\1'),
                                               ('test1', 'test 2'),
                                               ('test2', 'tes\\\\t')])

            test_doc = '[@test1], [@test2] [@test] [@tet], [@test1\\], ' \
                       '\\[@test]'

            exp_res = 'test 2, tes\\\\t test\\1 [@tet], [@test1\\], \\[@test]'

            assert CommonRegister.get_constants_set() == {
                ('test', 'test\\1'), ('test1', 'test 2'),
                ('test2', 'tes\\\\t')}

            assert const_compile(test_doc) == exp_res
