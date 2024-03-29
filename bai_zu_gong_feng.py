# import os
# import adbutils

# adb = adbutils.AdbClient(host="127.0.0.1", port=5037)

# serial = "emulator-5566"
# device = adb.device(serial=serial)

# resolution = (540, 960)
# os.environ['DEVICE_SERIAL'] = serial
# os.environ['ROOT_DIR'] = f'FanRenXiuXianIcon_{resolution[0]}_{resolution[1]}'

# main_region_coords = (1364, 47, 540, 960)

# os.environ['MAIN_REGION_COORDS'] = ','.join(map(str, main_region_coords))

import time
import pyautogui
from utils_adb import get_game_page_coords, get_region_coords, click_region, wait_region
from coords_manager import BaseCoordsManager
from event_executor import BaseExecutor
from xiuxian_exception import TimeOutException

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

class BaiZuGongFengCoordsManager(BaseCoordsManager):
    def __init__(self, main_region_coords, resolution=(1080, 1920)):
        super().__init__(main_region_coords, resolution)

    def price_in_bzgf_store_coords(self):
        diff = (1631, 707, 35, 22)
        # diff = (567, 1306, 93, 46)
        # return self.calculate_relative_coords(diff)
        return diff
        
    def jie_meng_ling_qu_coords(self):
        diff = (816, 387, 150, 149)
        return self.calculate_relative_coords(diff)

class BaiZuGongFengExecutor(BaseExecutor):
    def __init__(self, bzgf_coords_manager: BaiZuGongFengCoordsManager, buy_times: int):
        super().__init__(bzgf_coords_manager, 'bai_zu_gong_feng')
        self.bzgf_coords_manager = bzgf_coords_manager
        self.buy_times = buy_times
        self.cat_dir = 'bai_zu_gong_feng'

    @wait_region
    def get_ling_qu_coords(self, wait_time, target_region, is_to_click, wait_time_before_click, to_raise_exception):
        return get_region_coords(
            'ling_qu',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_buy_icon_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'buy_icon',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_jie_shou_gong_feng_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'jie_shou_gong_feng',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_gong_feng_over_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'gong_feng_over',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    def execute(self):
        self.go_to_world()
        
        self.click_ri_chang()
        self.scroll_and_click(direction='down')

        self.get_ling_qu_coords(wait_time=2, target_region='领取百族供奉', is_to_click=True, 
                                wait_time_before_click=1, to_raise_exception=True)

        # 领取结盟礼物
        time.sleep(2)
        click_region(self.bzgf_coords_manager.jie_meng_ling_qu_coords(), seconds=3)
        click_region(self.bzgf_coords_manager.exit())

        if self.buy_times > 0:
            self.get_buy_icon_coords(wait_time=5, target_region='购买图标', is_to_click=True, to_raise_exception=True)
            self.buy_times_in_store(self.buy_times, 'buy_times_is_not_enough', 
                                    price_in_store_coords=self.bzgf_coords_manager.price_in_bzgf_store_coords(),
                                    price_to_times = {50: 0, 100: 1, 150: 2})
            click_region(self.bzgf_coords_manager.better_exit())

        # 接受供奉
        start_time = time.time()
        while True:
            if time.time() - start_time > 120:
                raise TimeOutException('供奉超时!')

            self.get_jie_shou_gong_feng_coords(wait_time=2, 
                                               target_region='接受供奉', 
                                               is_to_click=True, 
                                               to_raise_exception=False)
            
            if self.if_buy_store_pop_up(confidence=0.7) is True:
                print('购买弹窗出现!')
                break

            
            gong_feng_over_coords = self.get_gong_feng_over_coords(wait_time=2,
                                                                   target_region='接受供奉结束', 
                                                                   is_to_click=False, 
                                                                   to_raise_exception=False)
            if gong_feng_over_coords:
                print('接受供奉结束!')
                break

if __name__ == '__main__':

    # resolution = (1080, 1920) # (width, height): (554, 984) or (1080, 1920)
    # main_region_coords = get_game_page_coords(resolution = resolution)

    # main_region_coords = tuple(map(int, main_region_coords_dt[device_serial].split(',')))

    coords_manager = BaiZuGongFengCoordsManager(main_region_coords, resolution=resolution)
    executor = BaiZuGongFengExecutor(coords_manager, buy_times=0)

    executor.execute()

