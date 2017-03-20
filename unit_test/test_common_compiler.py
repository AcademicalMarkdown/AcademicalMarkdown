import yaml
from frozendict import frozendict

from src.compilers.common_compilers.header_compiler import HeaderCompiler
from src.registers.common_register import CommonRegister
from unit_test.helpers.constants_for_test import test_yaml_with_minus_ending, \
    test_yaml_with_output_conf


class TestHeaderCompiler:
    def test_minus_ending(self):
        CommonRegister.__clear__()

        compiler = HeaderCompiler()
        compiler.load_header(
            header_yaml=test_yaml_with_minus_ending
        )

        exp_const = {('test', 'test1'), ('test1', 'test 2')}
        exp_output_conf = set()
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
        exp_output_conf = {frozendict({'format': 'latex', 'default': True}),
                           frozendict({'format': 'HTML', 'default': True})}
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
