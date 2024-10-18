
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTleftBWORleftBWXORleftBWANDrightQMARKCOLONnonassocEQNEEQ_FZMEQ_FZSNE_FZMNE_FZSGEGTLELTINleftADDSUBleftBWLSHBWRSHleftMULTDIVFDIVMODleftPOWrightUMINUSleftATTRATTR_SAFEnonassocLPARENRPARENADD AND ATTR ATTR_SAFE BWAND BWLSH BWOR BWRSH BWXOR BYTES COLON COMMA COMMENT DATETIME EQ EQ_FZM EQ_FZS FALSE FDIV FLOAT FLOAT_INF FLOAT_NAN FOR GE GT IF IN LBRACE LBRACKET LE LPAREN LT MOD MUL NE NE_FZM NE_FZS NOT NULL OR POW QMARK RBRACE RBRACKET RPAREN STRING SUB SYMBOL TDIV TIMEDELTA TRUE\n\t\tstatement : expression\n\t\t          | expression COMMENT\n\t\t\n\t\tobject : object ATTR SYMBOL\n\t\t       | object ATTR_SAFE SYMBOL\n\t\t\n\t\texpression : object\n\t\t\n\t\texpression : expression QMARK expression COLON expression\n\t\t\n\t\texpression : expression MOD    expression\n\t\t\t\t   | expression MUL    expression\n\t\t\t\t   | expression FDIV   expression\n\t\t\t\t   | expression TDIV   expression\n\t\t\t\t   | expression POW    expression\n\t\t\n\t\texpression : expression ADD    expression\n\t\t\n\t\texpression : expression SUB    expression\n\t\t\n\t\texpression : expression BWAND  expression\n\t\t\t\t   | expression BWOR   expression\n\t\t\t\t   | expression BWXOR  expression\n\t\t\n\t\texpression : expression BWLSH  expression\n\t\t\t\t   | expression BWRSH  expression\n\t\t\n\t\texpression : expression IN     expression\n\t\t\t\t   | expression NOT IN expression\n\t\t\n\t\texpression : expression EQ     expression\n\t\t\t\t   | expression NE     expression\n\t\t\n\t\texpression : expression GT     expression\n\t\t\t\t   | expression GE     expression\n\t\t\t\t   | expression LT     expression\n\t\t\t\t   | expression LE     expression\n\t\t\n\t\texpression : expression EQ_FZM expression\n\t\t\t\t   | expression EQ_FZS expression\n\t\t\t\t   | expression NE_FZM expression\n\t\t\t\t   | expression NE_FZS expression\n\t\t\n\t\texpression : expression AND    expression\n\t\t\t\t   | expression OR     expression\n\t\tobject : LPAREN expression RPARENexpression : NOT expressionobject : SYMBOLexpression : SUB expression %prec UMINUS\n\t\texpression : TRUE\n\t\t\t\t   | FALSE\n\t\tobject : BYTESobject : DATETIMEobject : TIMEDELTA\n\t\texpression : FLOAT\n\t\t\t\t   | FLOAT_NAN\n\t\t\t\t   | FLOAT_INF\n\t\tobject : NULL\n\t\tobject : LBRACE ary_members RBRACE\n\t\t\t   | LBRACE ary_members COMMA RBRACE\n\t\tobject : STRING\n\t\tobject : LBRACKET RBRACKET\n\t\t\t   | LBRACKET ary_members RBRACKET\n\t\t\t   | LBRACKET ary_members COMMA RBRACKET\n\t\t\n\t\tobject : LBRACKET expression FOR SYMBOL IN expression RBRACKET\n\t\t\t   | LBRACKET expression FOR SYMBOL IN expression IF expression RBRACKET\n\t\t\n\t\tary_members : expression\n\t\t\t\t\t| ary_members COMMA expression\n\t\t\n\t\tobject : LBRACE RBRACE\n\t\t\t   | LBRACE map_members RBRACE\n\t\t\t   | LBRACE map_members COMMA RBRACE\n\t\t\n\t\tmap_member : expression COLON expression\n\t\t\n\t\tmap_members : map_member\n\t\t\t\t\t| map_members COMMA map_member\n\t\t\n\t\tobject : object LBRACKET expression RBRACKET\n\t\t\n\t\tobject : object LBRACKET COLON RBRACKET\n\t\t       | object LBRACKET COLON expression RBRACKET\n\t\t       | object LBRACKET expression COLON RBRACKET\n\t\t       | object LBRACKET expression COLON expression RBRACKET\n\t\t\n\t\tobject : expression LPAREN RPAREN\n\t\t       | expression LPAREN ary_members RPAREN\n\t\t'
    
_lr_action_items = {'NOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,127,128,129,130,131,132,],[5,35,-5,5,5,-37,-38,-42,-43,-44,-35,5,-39,-40,-41,-45,5,-48,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-36,35,35,-56,35,-49,35,35,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,5,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,35,35,35,-67,-3,-4,35,5,-33,-46,5,-57,5,5,-50,5,5,-20,-68,5,-62,5,-63,35,-47,35,-58,35,35,-51,-6,35,-65,-64,5,-66,35,-52,5,35,-53,]),'SUB':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,127,128,129,130,131,132,],[4,28,-5,4,4,-37,-38,-42,-43,-44,-35,4,-39,-40,-41,-45,4,-48,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-36,28,28,-56,28,-49,28,28,-7,-8,-9,-10,-11,-12,-13,28,28,28,-17,-18,28,4,28,28,28,28,28,28,28,28,28,28,28,28,28,-67,-3,-4,28,4,-33,-46,4,-57,4,4,-50,4,4,28,-68,4,-62,4,-63,28,-47,28,-58,28,28,-51,28,28,-65,-64,4,-66,28,-52,4,28,-53,]),'TRUE':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'FALSE':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'FLOAT':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FLOAT_NAN':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'FLOAT_INF':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,111,112,113,114,115,116,118,119,120,122,123,124,125,126,127,128,129,130,131,132,],[12,48,-5,12,12,-37,-38,-42,-43,-44,-35,12,-39,-40,-41,-45,12,-48,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,48,48,48,-56,48,-49,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,12,48,48,48,48,48,48,48,48,48,48,48,48,48,-67,-3,-4,48,12,-33,-46,12,-57,12,12,-50,12,12,48,-68,12,-62,12,-63,48,-47,48,-58,48,48,-51,48,48,-65,-64,12,-66,48,-52,12,48,-53,]),'SYMBOL':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,77,96,99,101,102,104,105,106,109,111,126,130,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,93,94,11,11,11,11,11,11,11,121,11,11,11,11,11,]),'BYTES':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'DATETIME':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'TIMEDELTA':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'NULL':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'LBRACE':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'STRING':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'LBRACKET':([0,3,4,5,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,56,60,77,91,93,94,96,97,98,99,100,101,102,103,104,106,108,109,110,111,112,114,116,120,124,125,126,127,129,130,132,],[19,51,19,19,-35,19,-39,-40,-41,-45,19,-48,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-56,-49,19,-67,-3,-4,19,-33,-46,19,-57,19,19,-50,19,19,-68,19,-62,19,-63,-47,-58,-51,-65,-64,19,-66,-52,19,-53,]),'$end':([1,2,3,6,7,8,9,10,11,13,14,15,16,18,20,52,53,56,60,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,97,98,100,103,107,108,110,112,114,116,120,122,124,125,127,129,132,],[0,-1,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-2,-36,-34,-56,-49,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,-33,-46,-57,-50,-20,-68,-62,-63,-47,-58,-51,-6,-65,-64,-66,-52,-53,]),'COMMENT':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,56,60,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,97,98,100,103,107,108,110,112,114,116,120,122,124,125,127,129,132,],[20,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,-34,-56,-49,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,-33,-46,-57,-50,-20,-68,-62,-63,-47,-58,-51,-6,-65,-64,-66,-52,-53,]),'QMARK':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[21,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,21,21,-56,21,-49,21,21,-7,-8,-9,-10,-11,-12,-13,21,21,21,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,21,21,21,-67,-3,-4,21,-33,-46,-57,-50,-20,-68,-62,-63,21,-47,21,-58,21,21,-51,21,21,-65,-64,-66,21,-52,21,-53,]),'MOD':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[22,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,22,22,-56,22,-49,22,22,-7,-8,-9,-10,-11,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-67,-3,-4,22,-33,-46,-57,-50,22,-68,-62,-63,22,-47,22,-58,22,22,-51,22,22,-65,-64,-66,22,-52,22,-53,]),'MUL':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[23,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,23,23,-56,23,-49,23,23,-7,-8,-9,-10,-11,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-67,-3,-4,23,-33,-46,-57,-50,23,-68,-62,-63,23,-47,23,-58,23,23,-51,23,23,-65,-64,-66,23,-52,23,-53,]),'FDIV':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[24,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,24,24,-56,24,-49,24,24,-7,-8,-9,-10,-11,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-67,-3,-4,24,-33,-46,-57,-50,24,-68,-62,-63,24,-47,24,-58,24,24,-51,24,24,-65,-64,-66,24,-52,24,-53,]),'TDIV':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[25,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,25,25,-56,25,-49,25,25,-7,-8,-9,-10,-11,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-67,-3,-4,25,-33,-46,-57,-50,25,-68,-62,-63,25,-47,25,-58,25,25,-51,25,25,-65,-64,-66,25,-52,25,-53,]),'POW':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[26,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,26,26,-56,26,-49,26,26,26,26,26,26,-11,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-67,-3,-4,26,-33,-46,-57,-50,26,-68,-62,-63,26,-47,26,-58,26,26,-51,26,26,-65,-64,-66,26,-52,26,-53,]),'ADD':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[27,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,27,27,-56,27,-49,27,27,-7,-8,-9,-10,-11,-12,-13,27,27,27,-17,-18,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-67,-3,-4,27,-33,-46,-57,-50,27,-68,-62,-63,27,-47,27,-58,27,27,-51,27,27,-65,-64,-66,27,-52,27,-53,]),'BWAND':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[29,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,29,29,-56,29,-49,29,29,-7,-8,-9,-10,-11,-12,-13,-14,29,29,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,29,29,29,-67,-3,-4,29,-33,-46,-57,-50,-20,-68,-62,-63,29,-47,29,-58,29,29,-51,-6,29,-65,-64,-66,29,-52,29,-53,]),'BWOR':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[30,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,30,30,-56,30,-49,30,30,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,30,30,30,-67,-3,-4,30,-33,-46,-57,-50,-20,-68,-62,-63,30,-47,30,-58,30,30,-51,-6,30,-65,-64,-66,30,-52,30,-53,]),'BWXOR':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[31,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,31,31,-56,31,-49,31,31,-7,-8,-9,-10,-11,-12,-13,-14,31,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,31,31,31,-67,-3,-4,31,-33,-46,-57,-50,-20,-68,-62,-63,31,-47,31,-58,31,31,-51,-6,31,-65,-64,-66,31,-52,31,-53,]),'BWLSH':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[32,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,32,32,-56,32,-49,32,32,-7,-8,-9,-10,-11,32,32,32,32,32,-17,-18,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-67,-3,-4,32,-33,-46,-57,-50,32,-68,-62,-63,32,-47,32,-58,32,32,-51,32,32,-65,-64,-66,32,-52,32,-53,]),'BWRSH':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[33,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,33,33,-56,33,-49,33,33,-7,-8,-9,-10,-11,33,33,33,33,33,-17,-18,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-67,-3,-4,33,-33,-46,-57,-50,33,-68,-62,-63,33,-47,33,-58,33,33,-51,33,33,-65,-64,-66,33,-52,33,-53,]),'IN':([2,3,6,7,8,9,10,11,13,14,15,16,18,35,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,121,122,123,124,125,127,128,129,131,132,],[34,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,77,-36,34,34,-56,34,-49,34,34,-7,-8,-9,-10,-11,-12,-13,34,34,34,-17,-18,None,None,None,None,None,None,None,None,None,None,None,34,34,34,-67,-3,-4,34,-33,-46,-57,-50,None,-68,-62,-63,34,-47,34,-58,34,34,-51,126,34,34,-65,-64,-66,34,-52,34,-53,]),'EQ':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[36,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,36,36,-56,36,-49,36,36,-7,-8,-9,-10,-11,-12,-13,36,36,36,-17,-18,None,None,None,None,None,None,None,None,None,None,None,36,36,36,-67,-3,-4,36,-33,-46,-57,-50,None,-68,-62,-63,36,-47,36,-58,36,36,-51,36,36,-65,-64,-66,36,-52,36,-53,]),'NE':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[37,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,37,37,-56,37,-49,37,37,-7,-8,-9,-10,-11,-12,-13,37,37,37,-17,-18,None,None,None,None,None,None,None,None,None,None,None,37,37,37,-67,-3,-4,37,-33,-46,-57,-50,None,-68,-62,-63,37,-47,37,-58,37,37,-51,37,37,-65,-64,-66,37,-52,37,-53,]),'GT':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[38,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,38,38,-56,38,-49,38,38,-7,-8,-9,-10,-11,-12,-13,38,38,38,-17,-18,None,None,None,None,None,None,None,None,None,None,None,38,38,38,-67,-3,-4,38,-33,-46,-57,-50,None,-68,-62,-63,38,-47,38,-58,38,38,-51,38,38,-65,-64,-66,38,-52,38,-53,]),'GE':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[39,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,39,39,-56,39,-49,39,39,-7,-8,-9,-10,-11,-12,-13,39,39,39,-17,-18,None,None,None,None,None,None,None,None,None,None,None,39,39,39,-67,-3,-4,39,-33,-46,-57,-50,None,-68,-62,-63,39,-47,39,-58,39,39,-51,39,39,-65,-64,-66,39,-52,39,-53,]),'LT':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[40,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,40,40,-56,40,-49,40,40,-7,-8,-9,-10,-11,-12,-13,40,40,40,-17,-18,None,None,None,None,None,None,None,None,None,None,None,40,40,40,-67,-3,-4,40,-33,-46,-57,-50,None,-68,-62,-63,40,-47,40,-58,40,40,-51,40,40,-65,-64,-66,40,-52,40,-53,]),'LE':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[41,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,41,41,-56,41,-49,41,41,-7,-8,-9,-10,-11,-12,-13,41,41,41,-17,-18,None,None,None,None,None,None,None,None,None,None,None,41,41,41,-67,-3,-4,41,-33,-46,-57,-50,None,-68,-62,-63,41,-47,41,-58,41,41,-51,41,41,-65,-64,-66,41,-52,41,-53,]),'EQ_FZM':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[42,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,42,42,-56,42,-49,42,42,-7,-8,-9,-10,-11,-12,-13,42,42,42,-17,-18,None,None,None,None,None,None,None,None,None,None,None,42,42,42,-67,-3,-4,42,-33,-46,-57,-50,None,-68,-62,-63,42,-47,42,-58,42,42,-51,42,42,-65,-64,-66,42,-52,42,-53,]),'EQ_FZS':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[43,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,43,43,-56,43,-49,43,43,-7,-8,-9,-10,-11,-12,-13,43,43,43,-17,-18,None,None,None,None,None,None,None,None,None,None,None,43,43,43,-67,-3,-4,43,-33,-46,-57,-50,None,-68,-62,-63,43,-47,43,-58,43,43,-51,43,43,-65,-64,-66,43,-52,43,-53,]),'NE_FZM':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[44,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,44,44,-56,44,-49,44,44,-7,-8,-9,-10,-11,-12,-13,44,44,44,-17,-18,None,None,None,None,None,None,None,None,None,None,None,44,44,44,-67,-3,-4,44,-33,-46,-57,-50,None,-68,-62,-63,44,-47,44,-58,44,44,-51,44,44,-65,-64,-66,44,-52,44,-53,]),'NE_FZS':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[45,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,45,45,-56,45,-49,45,45,-7,-8,-9,-10,-11,-12,-13,45,45,45,-17,-18,None,None,None,None,None,None,None,None,None,None,None,45,45,45,-67,-3,-4,45,-33,-46,-57,-50,None,-68,-62,-63,45,-47,45,-58,45,45,-51,45,45,-65,-64,-66,45,-52,45,-53,]),'AND':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[46,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,-34,46,-56,46,-49,46,46,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,46,46,-67,-3,-4,46,-33,-46,-57,-50,-20,-68,-62,-63,46,-47,46,-58,46,46,-51,-6,46,-65,-64,-66,46,-52,46,-53,]),'OR':([2,3,6,7,8,9,10,11,13,14,15,16,18,52,53,54,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,97,98,100,103,107,108,110,112,113,114,115,116,118,119,120,122,123,124,125,127,128,129,131,132,],[47,-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,-34,47,-56,47,-49,47,47,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,47,-67,-3,-4,47,-33,-46,-57,-50,-20,-68,-62,-63,47,-47,47,-58,47,47,-51,-6,47,-65,-64,-66,47,-52,47,-53,]),'RPAREN':([3,6,7,8,9,10,11,13,14,15,16,18,48,52,53,54,56,60,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,100,103,107,108,110,112,114,115,116,120,122,124,125,127,129,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,91,-36,-34,97,-56,-49,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-54,-67,108,-3,-4,-33,-46,-57,-50,-20,-68,-62,-63,-47,-55,-58,-51,-6,-65,-64,-66,-52,-53,]),'COLON':([3,6,7,8,9,10,11,13,14,15,16,18,51,52,53,56,58,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,97,98,100,103,107,108,110,112,114,116,118,120,122,124,125,127,129,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,96,-36,-34,-56,102,-49,106,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,111,-33,-46,-57,-50,-20,-68,-62,-63,-47,-58,102,-51,-6,-65,-64,-66,-52,-53,]),'RBRACE':([3,6,7,8,9,10,11,13,14,15,16,17,18,52,53,55,56,57,58,59,60,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,97,98,99,100,101,103,107,108,110,112,114,115,116,117,119,120,122,124,125,127,129,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,56,-48,-36,-34,98,-56,100,-54,-60,-49,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,-33,-46,114,-57,116,-50,-20,-68,-62,-63,-47,-55,-58,-61,-59,-51,-6,-65,-64,-66,-52,-53,]),'COMMA':([3,6,7,8,9,10,11,13,14,15,16,18,52,53,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,100,103,107,108,110,112,114,115,116,117,119,120,122,124,125,127,129,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,-34,99,-56,101,-54,-60,-49,104,-54,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-54,-67,109,-3,-4,-33,-46,-57,-50,-20,-68,-62,-63,-47,-55,-58,-61,-59,-51,-6,-65,-64,-66,-52,-53,]),'FOR':([3,6,7,8,9,10,11,13,14,15,16,18,52,53,56,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,97,98,100,103,107,108,110,112,114,116,120,122,124,125,127,129,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,-34,-56,-49,105,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,-33,-46,-57,-50,-20,-68,-62,-63,-47,-58,-51,-6,-65,-64,-66,-52,-53,]),'RBRACKET':([3,6,7,8,9,10,11,13,14,15,16,18,19,52,53,56,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,97,98,100,103,104,107,108,110,111,112,113,114,115,116,120,122,123,124,125,127,128,129,131,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,60,-36,-34,-56,-49,103,-54,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,110,112,-33,-46,-57,-50,120,-20,-68,-62,124,-63,125,-47,-55,-58,-51,-6,127,-65,-64,-66,129,-52,132,-53,]),'IF':([3,6,7,8,9,10,11,13,14,15,16,18,52,53,56,60,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,97,98,100,103,107,108,110,112,114,116,120,122,124,125,127,128,129,132,],[-5,-37,-38,-42,-43,-44,-35,-39,-40,-41,-45,-48,-36,-34,-56,-49,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-67,-3,-4,-33,-46,-57,-50,-20,-68,-62,-63,-47,-58,-51,-6,-65,-64,-66,130,-52,-53,]),'ATTR':([3,11,13,14,15,16,18,56,60,91,93,94,97,98,100,103,108,110,112,114,116,120,124,125,127,129,132,],[49,-35,-39,-40,-41,-45,-48,-56,-49,-67,-3,-4,-33,-46,-57,-50,-68,-62,-63,-47,-58,-51,-65,-64,-66,-52,-53,]),'ATTR_SAFE':([3,11,13,14,15,16,18,56,60,91,93,94,97,98,100,103,108,110,112,114,116,120,124,125,127,129,132,],[50,-35,-39,-40,-41,-45,-48,-56,-49,-67,-3,-4,-33,-46,-57,-50,-68,-62,-63,-47,-58,-51,-65,-64,-66,-52,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[2,52,53,54,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,107,113,115,118,119,115,122,115,123,128,131,]),'object':([0,4,5,12,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,77,96,99,101,102,104,106,109,111,126,130,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'ary_members':([17,19,48,],[55,61,92,]),'map_members':([17,],[57,]),'map_member':([17,101,],[59,117,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','__init__.py',257),
  ('statement -> expression COMMENT','statement',2,'p_statement_expr','__init__.py',258),
  ('object -> object ATTR SYMBOL','object',3,'p_expression_getattr','__init__.py',267),
  ('object -> object ATTR_SAFE SYMBOL','object',3,'p_expression_getattr','__init__.py',268),
  ('expression -> object','expression',1,'p_expression_object','__init__.py',275),
  ('expression -> expression QMARK expression COLON expression','expression',5,'p_expression_ternary','__init__.py',281),
  ('expression -> expression MOD expression','expression',3,'p_expression_arithmetic','__init__.py',288),
  ('expression -> expression MUL expression','expression',3,'p_expression_arithmetic','__init__.py',289),
  ('expression -> expression FDIV expression','expression',3,'p_expression_arithmetic','__init__.py',290),
  ('expression -> expression TDIV expression','expression',3,'p_expression_arithmetic','__init__.py',291),
  ('expression -> expression POW expression','expression',3,'p_expression_arithmetic','__init__.py',292),
  ('expression -> expression ADD expression','expression',3,'p_expression_add','__init__.py',300),
  ('expression -> expression SUB expression','expression',3,'p_expression_sub','__init__.py',308),
  ('expression -> expression BWAND expression','expression',3,'p_expression_bitwise','__init__.py',316),
  ('expression -> expression BWOR expression','expression',3,'p_expression_bitwise','__init__.py',317),
  ('expression -> expression BWXOR expression','expression',3,'p_expression_bitwise','__init__.py',318),
  ('expression -> expression BWLSH expression','expression',3,'p_expression_bitwise_shift','__init__.py',326),
  ('expression -> expression BWRSH expression','expression',3,'p_expression_bitwise_shift','__init__.py',327),
  ('expression -> expression IN expression','expression',3,'p_expression_contains','__init__.py',335),
  ('expression -> expression NOT IN expression','expression',4,'p_expression_contains','__init__.py',336),
  ('expression -> expression EQ expression','expression',3,'p_expression_comparison','__init__.py',348),
  ('expression -> expression NE expression','expression',3,'p_expression_comparison','__init__.py',349),
  ('expression -> expression GT expression','expression',3,'p_expression_arithmetic_comparison','__init__.py',357),
  ('expression -> expression GE expression','expression',3,'p_expression_arithmetic_comparison','__init__.py',358),
  ('expression -> expression LT expression','expression',3,'p_expression_arithmetic_comparison','__init__.py',359),
  ('expression -> expression LE expression','expression',3,'p_expression_arithmetic_comparison','__init__.py',360),
  ('expression -> expression EQ_FZM expression','expression',3,'p_expression_fuzzy_comparison','__init__.py',368),
  ('expression -> expression EQ_FZS expression','expression',3,'p_expression_fuzzy_comparison','__init__.py',369),
  ('expression -> expression NE_FZM expression','expression',3,'p_expression_fuzzy_comparison','__init__.py',370),
  ('expression -> expression NE_FZS expression','expression',3,'p_expression_fuzzy_comparison','__init__.py',371),
  ('expression -> expression AND expression','expression',3,'p_expression_logic','__init__.py',379),
  ('expression -> expression OR expression','expression',3,'p_expression_logic','__init__.py',380),
  ('object -> LPAREN expression RPAREN','object',3,'p_expression_group','__init__.py',387),
  ('expression -> NOT expression','expression',2,'p_expression_negate','__init__.py',391),
  ('object -> SYMBOL','object',1,'p_expression_symbol','__init__.py',395),
  ('expression -> SUB expression','expression',2,'p_expression_uminus','__init__.py',404),
  ('expression -> TRUE','expression',1,'p_expression_boolean','__init__.py',411),
  ('expression -> FALSE','expression',1,'p_expression_boolean','__init__.py',412),
  ('object -> BYTES','object',1,'p_expression_bytes','__init__.py',417),
  ('object -> DATETIME','object',1,'p_expression_datetime','__init__.py',421),
  ('object -> TIMEDELTA','object',1,'p_expression_timedelta','__init__.py',425),
  ('expression -> FLOAT','expression',1,'p_expression_float','__init__.py',430),
  ('expression -> FLOAT_NAN','expression',1,'p_expression_float','__init__.py',431),
  ('expression -> FLOAT_INF','expression',1,'p_expression_float','__init__.py',432),
  ('object -> NULL','object',1,'p_expression_null','__init__.py',438),
  ('object -> LBRACE ary_members RBRACE','object',3,'p_expression_set','__init__.py',444),
  ('object -> LBRACE ary_members COMMA RBRACE','object',4,'p_expression_set','__init__.py',445),
  ('object -> STRING','object',1,'p_expression_string','__init__.py',450),
  ('object -> LBRACKET RBRACKET','object',2,'p_expression_array','__init__.py',455),
  ('object -> LBRACKET ary_members RBRACKET','object',3,'p_expression_array','__init__.py',456),
  ('object -> LBRACKET ary_members COMMA RBRACKET','object',4,'p_expression_array','__init__.py',457),
  ('object -> LBRACKET expression FOR SYMBOL IN expression RBRACKET','object',7,'p_expression_array_comprehension','__init__.py',466),
  ('object -> LBRACKET expression FOR SYMBOL IN expression IF expression RBRACKET','object',9,'p_expression_array_comprehension','__init__.py',467),
  ('ary_members -> expression','ary_members',1,'p_expression_array_members','__init__.py',476),
  ('ary_members -> ary_members COMMA expression','ary_members',3,'p_expression_array_members','__init__.py',477),
  ('object -> LBRACE RBRACE','object',2,'p_expression_mapping','__init__.py',489),
  ('object -> LBRACE map_members RBRACE','object',3,'p_expression_mapping','__init__.py',490),
  ('object -> LBRACE map_members COMMA RBRACE','object',4,'p_expression_mapping','__init__.py',491),
  ('map_member -> expression COLON expression','map_member',3,'p_expression_mapping_member','__init__.py',500),
  ('map_members -> map_member','map_members',1,'p_expression_mapping_members','__init__.py',506),
  ('map_members -> map_members COMMA map_member','map_members',3,'p_expression_mapping_members','__init__.py',507),
  ('object -> object LBRACKET expression RBRACKET','object',4,'p_expression_getitem','__init__.py',513),
  ('object -> object LBRACKET COLON RBRACKET','object',4,'p_expression_getslice','__init__.py',520),
  ('object -> object LBRACKET COLON expression RBRACKET','object',5,'p_expression_getslice','__init__.py',521),
  ('object -> object LBRACKET expression COLON RBRACKET','object',5,'p_expression_getslice','__init__.py',522),
  ('object -> object LBRACKET expression COLON expression RBRACKET','object',6,'p_expression_getslice','__init__.py',523),
  ('object -> expression LPAREN RPAREN','object',3,'p_expression_function_call','__init__.py',542),
  ('object -> expression LPAREN ary_members RPAREN','object',4,'p_expression_function_call','__init__.py',543),
]
