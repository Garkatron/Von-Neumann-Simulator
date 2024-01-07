
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUALS FUNCTION LBRACKET LPAREN NAME NUMBER RBRACKET RPARENexpressions : expression\n                   | expressions expressionstatement : FUNCTION NAME LBRACKET expression RBRACKET\n                | FUNCTION NAME LBRACKET RBRACKET\n                | FUNCTION NAME LBRACKET expressions RBRACKETstatement : NAME EQUALS expressionsstatement : expressionexpression : LBRACKET RBRACKETexpression : LBRACKET expression RBRACKET\n                | LBRACKET expressions RBRACKETexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'LBRACKET':([0,1,2,3,4,5,6,7,8,9,10,11,],[3,3,-1,3,-11,-12,-2,-8,-1,3,-9,-10,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,],[4,4,-1,4,-11,-12,-2,-8,-1,4,-9,-10,]),'NAME':([0,1,2,3,4,5,6,7,8,9,10,11,],[5,5,-1,5,-11,-12,-2,-8,-1,5,-9,-10,]),'$end':([1,2,4,5,6,7,10,11,],[0,-1,-11,-12,-2,-8,-9,-10,]),'RBRACKET':([3,4,5,6,7,8,9,10,11,],[7,-11,-12,-2,-8,10,11,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,3,],[1,9,]),'expression':([0,1,3,9,],[2,6,8,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression','expressions',1,'p_expressions','main.py',69),
  ('expressions -> expressions expression','expressions',2,'p_expressions','main.py',70),
  ('statement -> FUNCTION NAME LBRACKET expression RBRACKET','statement',5,'p_statement_function','main.py',78),
  ('statement -> FUNCTION NAME LBRACKET RBRACKET','statement',4,'p_statement_function','main.py',79),
  ('statement -> FUNCTION NAME LBRACKET expressions RBRACKET','statement',5,'p_statement_function','main.py',80),
  ('statement -> NAME EQUALS expressions','statement',3,'p_statement_assign','main.py',87),
  ('statement -> expression','statement',1,'p_statement_expr','main.py',92),
  ('expression -> LBRACKET RBRACKET','expression',2,'p_expression_group','main.py',96),
  ('expression -> LBRACKET expression RBRACKET','expression',3,'p_expression_non_empty_group','main.py',100),
  ('expression -> LBRACKET expressions RBRACKET','expression',3,'p_expression_non_empty_group','main.py',101),
  ('expression -> NUMBER','expression',1,'p_expression_number','main.py',106),
  ('expression -> NAME','expression',1,'p_expression_name','main.py',110),
]