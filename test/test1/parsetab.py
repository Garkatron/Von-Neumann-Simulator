
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DIVIDE FUNCTION ID LBRACKET LPAREN MEMPOS MINUS NEWLINE NUMBER PLUS PRT RBRACKET RPAREN STRING TIMESstatement : PRT MEMPOSempty :statements : statements statement\n                | statement\n                | emptycode_block : LBRACKET statements RBRACKET\n                | LBRACKET empty RBRACKET\n                | LBRACKET RBRACKETstatement : FUNCTION ID LBRACKET code_block RBRACKET'
    
_lr_action_items = {'PRT':([0,4,7,9,11,12,13,15,],[2,-1,2,2,-5,-4,-9,-3,]),'FUNCTION':([0,4,7,9,11,12,13,15,],[3,-1,3,3,-5,-4,-9,-3,]),'$end':([1,4,13,],[0,-1,-9,]),'MEMPOS':([2,],[4,]),'ID':([3,],[5,]),'RBRACKET':([4,7,8,9,10,11,12,13,14,15,16,],[-1,10,13,14,-8,16,-4,-9,-6,-3,-7,]),'LBRACKET':([5,6,],[6,7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,7,9,],[1,12,15,]),'code_block':([6,],[8,]),'statements':([7,],[9,]),'empty':([7,],[11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> PRT MEMPOS','statement',2,'p_expression_prt','main.py',103),
  ('empty -> <empty>','empty',0,'p_empty','main.py',107),
  ('statements -> statements statement','statements',2,'p_statements','main.py',112),
  ('statements -> statement','statements',1,'p_statements','main.py',113),
  ('statements -> empty','statements',1,'p_statements','main.py',114),
  ('code_block -> LBRACKET statements RBRACKET','code_block',3,'p_code_block','main.py',124),
  ('code_block -> LBRACKET empty RBRACKET','code_block',3,'p_code_block','main.py',125),
  ('code_block -> LBRACKET RBRACKET','code_block',2,'p_code_block','main.py',126),
  ('statement -> FUNCTION ID LBRACKET code_block RBRACKET','statement',5,'p_expression_func','main.py',133),
]