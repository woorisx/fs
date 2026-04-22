
# 임포트 방법1) import 패키지명 모듈명
import game.sound.echo    
game.sound.echo.echo_test() # echo
print('-'*20)

# 임포트 방법2) 패키지명 import 모듈명
from game.sound import echo
echo.echo_test() # echo
print('-'*20)

# 임포트 방법3) 패키지명 import 함수명
from game.sound.echo import echo_test
echo_test() # echo

