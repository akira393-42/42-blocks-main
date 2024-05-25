import time
from ss_player.Board import Board
from ss_player.Blocks import Blocks
from ss_player.Position import Position
from ss_player.Player import Player
from ss_player.BlockType import BlockType
from time import sleep
import numpy as np




# Board example o = player1, x = player2
#  123456789ABCDE
# 1..............
# 2..............
# 3..............
# 4...o..........
# 5..ooo.........
# 6...o..........
# 7..............
# 8..............
# 9..............
# A.........x....
# B..............
# C..............
# D..............
# E..............

xystr = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E"]

class Logic:
    def get_available_actions(self,board:Board,blocks:Blocks,player:Player,turn:int):
        start_time=time.time()
        print(board.now_board())
        # is_first = not np.any(board.now_board() == player.player_number)

        if(turn == 1):
            blocks.block_used(BlockType.R)
            if(player.player_number == 1):
                return "R244"
            else:
                return "R699"
        for block in [block for block in blocks.blocks if block.block_type.value!='X']:

            print("player:",player.player_number,"block type:",block.block_type)

            # ブロックを置ける場所を探si,ループを一つにする
            for (x,y) in board.get_candidate_positions():

                print("x:",x,"y:",y)
            # for x in range(1,board.shape_x+1):
            #     for y in range(1,board.shape_y+1):
                # 座標x,yがすでに置かれている場合はスキップ
                if(board.now_board()[x-1][y-1] != 0):
                    continue

                padded_block = None
                try:
                    padded_block = board.PaddedBlock(board,block,Position(x,y))
                except Exception as e:
                    # TODO Errorハンドリング追加。　今は-1の場合にエラーになるのでTryCatchで回避
                    # print(e.__str__ == "index can't contain negative values")
                    # sleep(5)
                    continue

                if(board.can_place(player,padded_block)):
                    result = f"{block.block_type.value}{block.block_rotation.value}{xystr[x-1]}{xystr[y-1]}"
                    print("result")
                    print(result)
                    print("player num")
                    print(player.player_number)
                    blocks.block_used(block.block_type)
                    return result
            if time.time()-start_time>4.8:
                print("[info]: time out")
                break
        return "X000"
