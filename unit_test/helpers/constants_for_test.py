# this is a list of para that is not accepted by any model
other_para_list = [{'nuh': 'gosh'},
                   {'not-in-list': 'no, no, no'},
                   {'testing-no': 'ha ha ha lala'},
                   {'definitely-no': 'hahaha'}]

# ============== For Code Testing ===================

# when user specify file in the code block
code_test_dict_with_file = {'label': 'test_code',
                            'syntax': 'python',
                            'caption': 'this is a test code',
                            'file': './unit_test/resources/resource.py'}
# when user specify contnet in the code block
code_test_dict_with_content = {'label': 'test_code',
                               'syntax': 'coq',
                               'caption': 'this is a test code',
                               'content': 'Definition ayaya'}
# the required parameter for code block
code_req_para = ['syntax', 'caption']

constant_test_dict = {'label': 'constant1',
                      'content': 'this is the test to '
                                 'replace it with'}
constant_req_para = ['label', 'content']

figure_test_dict = {'label': 'fig:figid',
                    'source': './image/git.png',
                    'caption': 'this is a image',
                    'width': '30',
                    'height': '20',
                    'code': 'pass'}
figure_req_para = ['source', 'caption']

include_test_dict = {'file': 'src/test.md'}
include_req_para = ['file']

table_test_dict_with_file = {'file': './unit_test/resources/test.csv',
                             'top_header': True,
                             'caption': 'this is a table',
                             'label': 'tbl: testTable'}
table_req_para = ['top_header', 'caption']

theorem_test_dict = {'label': 'thm:maxwell eq',
                     'content': 'great theorem',
                     'theorem_type': 'Lemma'}
theorem_req_para = ['content']
