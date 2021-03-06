import asyncio
import functools
from datetime import datetime
import sys

#from PyQt5.QtWidgets import QApplication

class AutoRunDecorator:
    def __init__(self, func):
        self.func = func

    #def __call__(self, *args, **kwargs):
    #    app = QApplication(sys.argv) # 앱 실행
    #    self.func(*args, **kwargs) # 함수 실행
    #    sys.exit(app.exec_()) # 종료

    # 24시간 돌아가는 기능 coroutine decorator: ex(서버 상태 확인)
    @staticmethod
    def asyncFullTime(delay):
        def wrapper(func):
            @functools.wraps(func)
            async def inner(*args, **kwargs):
                while True:
                    try:
                        await asyncio.sleep(delay)
                        await func(*args, **kwargs)
                    except Exception as e:
                        print(e)
            return inner
        return wrapper

    @staticmethod
    def asyncSpotTime(startTime, deadline=20, delay=1):
        ''' 특정 1회만 실행되는 coroutin decorator, ex: 매수집행
        params
        =======================================
        startTime: str ,(HH:MM:SS, 24시간 단위로) ==> 실행 시간
        deadline: int,  deadline(초) 이내로 실행 못하면 실행 하지 않음
        delay: int, 시간 확인 주기(초)
        '''
        startTime = int(startTime.replace(':', '')) # 09:00:10 => 90010
        endTime = startTime + deadline

        def wrapper(func):
            @functools.wraps(func)
            async def inner(*args, **kwargs):
                while True:
                    curTime = int(datetime.now().strftime('%H%M%S')) # 090010 => 90010
                    if (startTime <= curTime) & (curTime <= endTime): # 지정한 시간이 되면 실행
                        try:
                            await func(*args, **kwargs)
                            break
                        except Exception as e:
                            print(e)
                    await asyncio.sleep(delay)
            return inner
        return wrapper