
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'moduleleftPLUSMINUSleftTIMESDIVIDEMODARROW NUMBER LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE SEMI COLON COLONS EQUAL COMMA EOF NAME PLUS MINUS TIMES DIVIDE MOD AND XOR OR GT LT GE LE EQ NE LSHIFT RSHIFT LAND LOR COMMENT PROCTYPE ACTIVE TRUE FALSE SKIP IF FI DO OD ATOMIC D_STEP INT PRINTM MTYPEmodule   : proctype\n                | mtype\n    proctype : active PROCTYPE name LPAREN RPAREN LBRACE sequence RBRACEactive   : ACTIVE\n                | ACTIVE LBRACKET const RBRACKETconst    : TRUE\n                | FALSE\n                | SKIP\n                | NUMBERname : NAMEsequence     : step\n                    | step SEMI sequencestep : stmntstmnt    : IF options FI\n                | DO options OD\n                | ATOMIC LBRACE sequence RBRACE\n                | D_STEP LBRACE sequence RBRACE\n                | LBRACE sequence RBRACE\n                | PRINTM LPAREN name RPAREN\n                | exproptions  : COLONS sequence\n                | COLONS sequence optionsmtype : MTYPE LBRACE names RBRACEnames    : name\n                | name COMMA namesany_expr : LPAREN any_expr RPAREN\n                | const\n                | any_expr binarop any_exprbinarop  : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MODexpr : any_expr\n            | LPAREN expr RPAREN\n    '
    
_lr_action_items = {'MTYPE':([0,],[5,]),'ACTIVE':([0,],[6,]),'$end':([1,2,3,20,42,],[0,-1,-2,-23,-3,]),'PROCTYPE':([4,6,22,],[7,-4,-5,]),'LBRACE':([5,23,25,27,33,34,43,45,47,48,],[8,25,27,27,47,48,27,27,27,27,]),'LBRACKET':([6,],[9,]),'NAME':([7,8,21,49,],[11,11,11,11,]),'TRUE':([9,25,26,27,43,45,47,48,50,51,52,53,54,55,67,],[15,15,15,15,15,15,15,15,15,-29,-30,-31,-32,-33,15,]),'FALSE':([9,25,26,27,43,45,47,48,50,51,52,53,54,55,67,],[16,16,16,16,16,16,16,16,16,-29,-30,-31,-32,-33,16,]),'SKIP':([9,25,26,27,43,45,47,48,50,51,52,53,54,55,67,],[17,17,17,17,17,17,17,17,17,-29,-30,-31,-32,-33,17,]),'NUMBER':([9,25,26,27,43,45,47,48,50,51,52,53,54,55,67,],[18,18,18,18,18,18,18,18,18,-29,-30,-31,-32,-33,18,]),'LPAREN':([10,11,25,26,27,35,43,45,47,48,50,51,52,53,54,55,67,],[19,-10,26,26,26,49,26,26,26,26,67,-29,-30,-31,-32,-33,67,]),'COMMA':([11,13,],[-10,21,]),'RBRACE':([11,12,13,15,16,17,18,24,28,29,30,36,37,38,41,56,57,58,59,60,62,63,64,66,69,70,71,],[-10,20,-24,-6,-7,-8,-9,-25,42,-11,-13,-20,-34,-27,58,-35,-26,-18,-12,-14,-15,69,70,-28,-16,-17,-19,]),'RPAREN':([11,15,16,17,18,19,38,39,40,56,57,65,66,72,],[-10,-6,-7,-8,-9,23,-27,56,57,-35,-26,71,-28,57,]),'RBRACKET':([14,15,16,17,18,],[22,-6,-7,-8,-9,]),'PLUS':([15,16,17,18,37,38,40,57,66,72,],[-6,-7,-8,-9,51,-27,51,-26,51,51,]),'MINUS':([15,16,17,18,37,38,40,57,66,72,],[-6,-7,-8,-9,52,-27,52,-26,52,52,]),'TIMES':([15,16,17,18,37,38,40,57,66,72,],[-6,-7,-8,-9,53,-27,53,-26,53,53,]),'DIVIDE':([15,16,17,18,37,38,40,57,66,72,],[-6,-7,-8,-9,54,-27,54,-26,54,54,]),'MOD':([15,16,17,18,37,38,40,57,66,72,],[-6,-7,-8,-9,55,-27,55,-26,55,55,]),'SEMI':([15,16,17,18,29,30,36,37,38,56,57,58,60,62,66,69,70,71,],[-6,-7,-8,-9,43,-13,-20,-34,-27,-35,-26,-18,-14,-15,-28,-16,-17,-19,]),'COLONS':([15,16,17,18,29,30,31,32,36,37,38,56,57,58,59,60,61,62,66,69,70,71,],[-6,-7,-8,-9,-11,-13,45,45,-20,-34,-27,-35,-26,-18,-12,-14,45,-15,-28,-16,-17,-19,]),'FI':([15,16,17,18,29,30,36,37,38,44,56,57,58,59,60,61,62,66,68,69,70,71,],[-6,-7,-8,-9,-11,-13,-20,-34,-27,60,-35,-26,-18,-12,-14,-21,-15,-28,-22,-16,-17,-19,]),'OD':([15,16,17,18,29,30,36,37,38,46,56,57,58,59,60,61,62,66,68,69,70,71,],[-6,-7,-8,-9,-11,-13,-20,-34,-27,62,-35,-26,-18,-12,-14,-21,-15,-28,-22,-16,-17,-19,]),'IF':([25,27,43,45,47,48,],[31,31,31,31,31,31,]),'DO':([25,27,43,45,47,48,],[32,32,32,32,32,32,]),'ATOMIC':([25,27,43,45,47,48,],[33,33,33,33,33,33,]),'D_STEP':([25,27,43,45,47,48,],[34,34,34,34,34,34,]),'PRINTM':([25,27,43,45,47,48,],[35,35,35,35,35,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'module':([0,],[1,]),'proctype':([0,],[2,]),'mtype':([0,],[3,]),'active':([0,],[4,]),'name':([7,8,21,49,],[10,13,13,65,]),'names':([8,21,],[12,24,]),'const':([9,25,26,27,43,45,47,48,50,67,],[14,38,38,38,38,38,38,38,38,38,]),'sequence':([25,27,43,45,47,48,],[28,41,59,61,63,64,]),'step':([25,27,43,45,47,48,],[29,29,29,29,29,29,]),'stmnt':([25,27,43,45,47,48,],[30,30,30,30,30,30,]),'expr':([25,26,27,43,45,47,48,],[36,39,36,36,36,36,36,]),'any_expr':([25,26,27,43,45,47,48,50,67,],[37,40,37,37,37,37,37,66,72,]),'options':([31,32,61,],[44,46,68,]),'binarop':([37,40,66,72,],[50,50,50,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> proctype','module',1,'p_module','lexer_ply.py',158),
  ('module -> mtype','module',1,'p_module','lexer_ply.py',159),
  ('proctype -> active PROCTYPE name LPAREN RPAREN LBRACE sequence RBRACE','proctype',8,'p_proctype','lexer_ply.py',164),
  ('active -> ACTIVE','active',1,'p_active','lexer_ply.py',172),
  ('active -> ACTIVE LBRACKET const RBRACKET','active',4,'p_active','lexer_ply.py',173),
  ('const -> TRUE','const',1,'p_const','lexer_ply.py',188),
  ('const -> FALSE','const',1,'p_const','lexer_ply.py',189),
  ('const -> SKIP','const',1,'p_const','lexer_ply.py',190),
  ('const -> NUMBER','const',1,'p_const','lexer_ply.py',191),
  ('name -> NAME','name',1,'p_name','lexer_ply.py',199),
  ('sequence -> step','sequence',1,'p_sequence','lexer_ply.py',207),
  ('sequence -> step SEMI sequence','sequence',3,'p_sequence','lexer_ply.py',208),
  ('step -> stmnt','step',1,'p_step','lexer_ply.py',222),
  ('stmnt -> IF options FI','stmnt',3,'p_stmnt','lexer_ply.py',226),
  ('stmnt -> DO options OD','stmnt',3,'p_stmnt','lexer_ply.py',227),
  ('stmnt -> ATOMIC LBRACE sequence RBRACE','stmnt',4,'p_stmnt','lexer_ply.py',228),
  ('stmnt -> D_STEP LBRACE sequence RBRACE','stmnt',4,'p_stmnt','lexer_ply.py',229),
  ('stmnt -> LBRACE sequence RBRACE','stmnt',3,'p_stmnt','lexer_ply.py',230),
  ('stmnt -> PRINTM LPAREN name RPAREN','stmnt',4,'p_stmnt','lexer_ply.py',231),
  ('stmnt -> expr','stmnt',1,'p_stmnt','lexer_ply.py',232),
  ('options -> COLONS sequence','options',2,'p_options','lexer_ply.py',257),
  ('options -> COLONS sequence options','options',3,'p_options','lexer_ply.py',258),
  ('mtype -> MTYPE LBRACE names RBRACE','mtype',4,'p_mtype','lexer_ply.py',273),
  ('names -> name','names',1,'p_names','lexer_ply.py',279),
  ('names -> name COMMA names','names',3,'p_names','lexer_ply.py',280),
  ('any_expr -> LPAREN any_expr RPAREN','any_expr',3,'p_any_expr','lexer_ply.py',288),
  ('any_expr -> const','any_expr',1,'p_any_expr','lexer_ply.py',289),
  ('any_expr -> any_expr binarop any_expr','any_expr',3,'p_any_expr','lexer_ply.py',290),
  ('binarop -> PLUS','binarop',1,'p_binarop','lexer_ply.py',348),
  ('binarop -> MINUS','binarop',1,'p_binarop','lexer_ply.py',349),
  ('binarop -> TIMES','binarop',1,'p_binarop','lexer_ply.py',350),
  ('binarop -> DIVIDE','binarop',1,'p_binarop','lexer_ply.py',351),
  ('binarop -> MOD','binarop',1,'p_binarop','lexer_ply.py',352),
  ('expr -> any_expr','expr',1,'p_expr','lexer_ply.py',372),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr','lexer_ply.py',373),
]
