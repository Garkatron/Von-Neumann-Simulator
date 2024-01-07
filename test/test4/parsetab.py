
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CALL EQUALS FUNCTION IDENTIFIER LBRACKET LPAREN NUMBER PLUS RBRACKET RPARENstatement : expressionstatement : IDENTIFIER EQUALS expressionexpression : expression PLUS expressionstatement : FUNCTION IDENTIFIER LBRACKET statements RBRACKET\n                | FUNCTION IDENTIFIER LBRACKET RBRACKETexpression : IDENTIFIERstatement : CALL IDENTIFIERexpression : NUMBERstatements : statements statement\n                | statement'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,],[3,-1,-6,9,10,-8,12,12,-7,-3,-6,-2,3,3,-5,-10,-4,-9,]),'FUNCTION':([0,2,3,6,10,11,12,13,14,15,16,17,18,19,],[4,-1,-6,-8,-7,-3,-6,-2,4,4,-5,-10,-4,-9,]),'CALL':([0,2,3,6,10,11,12,13,14,15,16,17,18,19,],[5,-1,-6,-8,-7,-3,-6,-2,5,5,-5,-10,-4,-9,]),'NUMBER':([0,2,3,6,7,8,10,11,12,13,14,15,16,17,18,19,],[6,-1,-6,-8,6,6,-7,-3,-6,-2,6,6,-5,-10,-4,-9,]),'$end':([1,2,3,6,10,11,12,13,16,18,],[0,-1,-6,-8,-7,-3,-6,-2,-5,-4,]),'RBRACKET':([2,3,6,10,11,12,13,14,15,16,17,18,19,],[-1,-6,-8,-7,-3,-6,-2,16,18,-5,-10,-4,-9,]),'PLUS':([2,3,6,11,12,13,],[7,-6,-8,7,-6,7,]),'EQUALS':([3,],[8,]),'LBRACKET':([9,],[14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,14,15,],[1,17,19,]),'expression':([0,7,8,14,15,],[2,11,13,2,2,]),'statements':([14,],[15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','main.py',88),
  ('statement -> IDENTIFIER EQUALS expression','statement',3,'p_statement_assing','main.py',93),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','main.py',101),
  ('statement -> FUNCTION IDENTIFIER LBRACKET statements RBRACKET','statement',5,'p_function_definition','main.py',107),
  ('statement -> FUNCTION IDENTIFIER LBRACKET RBRACKET','statement',4,'p_function_definition','main.py',108),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','main.py',122),
  ('statement -> CALL IDENTIFIER','statement',2,'p_statement_function_call','main.py',130),
  ('expression -> NUMBER','expression',1,'p_expression_number','main.py',143),
  ('statements -> statements statement','statements',2,'p_statement_multiple','main.py',148),
  ('statements -> statement','statements',1,'p_statement_multiple','main.py',149),
]