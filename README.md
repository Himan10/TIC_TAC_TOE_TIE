# TIC_TAC_TOE_TIE
You already know how to play the game and in case you don't then search it on google, darkweb or books(in your school library) i'm not writing any tutorial here about the game.

The game is in between our intelligent species(computer) and BIG-BOO(you-humans)
 
So let me give you little bit description about my tic-tac-toe, 
  1. You start playing it
  2. You make a move on the board
  3. Our intelligent species(computer) defeats you
  4. and that's it.. BIG-BOO've done it .. BIG-BOO lost .. and that's the motive of our game.

# HOW OUR INTELLIGENT SPECIES DEFEATING BIG-BOO's
   # Go for Corner-Center at first
   what i meant by this is, if you got a first chance to start the game then you should go for corners or centers but in case, you        ain't the first guy and second player make his move on corners then go for center. Avoid making your move on edges. 
        And that's what i do with my method i.e., i make a list of corners [1,3,7,9] and check either all corners are empty or not, if yes(means corners are empty) then computer make his random move on any corner but what if corners aren't empty? 
        Yeah, so our corners - [1,3,7,9] ain't empty. Now what we do is to make a computer's move on center - '5'.

        
        corner = [1,3,7,9]
        if all(board[c] == "     " for c in corner):
          return random.choice(corner)
        
        if board[5] == "     ": #for 5th(center) move
          return 5
        
   
   # Opponents move (CHECK IT AND BLOCK IT)
   Yeah, now our computer makes it move on corner or center. okay the next step is to check what type of moves our opponent(YOU BIG-BOO) makes. so here our computer isn't actually judging you or what moves you make instead it'll check patterns, Although you're free to make your any move on the board on your first chance. 
Okay, let's assume BIG-BOO goes first and make his move at 3rd block -> then computer make his move on center(5) -> then BIG-BOO place his 'x' or 'o' at 2nd block on the board. (So now everyone knows at which location our intelligent computer should make a move)
Now that's the point where our large conditional statements start to unleash it's dark side. means we know where he do but let's talk about how he do it. So in a tic-tac-toe board we've some patterns (Horizontally, Vertically and Diagonally) like:
        
        Horizontally: (1,2,3), (4,5,6), (7,8,9)
        Vertically:   (1,4,7), (2,5,8), (3,6,9)
        Diagonally:   (3,5,7), (1,5,9)

and now our intelligent species(Computer) can look up on these patterns to make it's new move and BLOCK the opponent move, so if we look backward (in previous lines) we can see that our user already made his 2nd move at 2nd position on the board, So, how can our computer make his next move to block the user or simply say (to stop user not to WIN) here's the mantra of it --- 

         if board[1] == "     ":  # for 1st move
             if (
                 board[2] == turn and board[3] == turn or
                 board[4] == turn and board[7] == turn or
                 board[5] == turn and board[9] == turn
            ):
             return 1
Those who're familiar with conditional statements can easily figure it out how our computer block the 1st position and it does the same for upcoming patterns... 

   # Some Advanced Algorithms
   -> Alpha-Beta Pruning - https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

   -> Min-Max Algorithm  - https://en.wikipedia.org/wiki/Minimax
   
and let me tell you clearly that what've done isn't have any advanced algorithms or anything. it's just a bunch of large conditional statements and the most important thing is, still the code isn't too much accurate to predict and block the moves which results in, BIG-BOO(user) can win on some cases but i'm on my way to upgrade it and making an advanced version of it i.e., 

   Ultimate TIC-TAC-TOE   - https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe
   
 THANK YOU 
