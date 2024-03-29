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

import pyautogui
import time
from utils_adb import get_game_page_coords, get_region_coords, click_region, wait_region, scroll_specific_length
from coords_manager import BaseCoordsManager
from event_executor import BaseExecutor
from xiuxian_exception import ShuangXiuException

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

class ShuangXiuCoordsManager(BaseCoordsManager):
    def __init__(self, main_region_coords, resolution=(1080, 1920)):
        super().__init__(main_region_coords, resolution)

    def yaoqing_daoyou(self): # 双修界面-邀请道友按钮
        diff = (478, 1447, 127, 127)
        return self.calculate_relative_coords(diff)
    
    def yaoqing_region(self): # 仙缘邀请界面-邀请区域
        diff = (772, 477, 193, 971)
        return self.calculate_relative_coords(diff)
    
    def go_to_xiulian(self): # 双修界面-前往修炼按钮
        diff = (287, 1644, 510, 101)
        return self.calculate_relative_coords(diff)

    def xianyuan_page(self): # 双修界面-仙缘界面
        diff = (314, 398, 162, 76)
        return self.calculate_relative_coords(diff)
    
    def remain_times(self):
        diff = (702, 1585, 41, 45)
        return self.calculate_relative_coords(diff)

class ShuangXiuExecutor(BaseExecutor):
    def __init__(
        self,
        shuangxiu_coords_manager: ShuangXiuCoordsManager,
        gongfashu_name: str
    ):
        super().__init__(shuangxiu_coords_manager, 'shuangxiu')

        self.shuangxiu_coords_manager = shuangxiu_coords_manager
        self.gongfashu_name = gongfashu_name
        self.gongfashu_name_dict = {
            '引龙诀': 'yin_long_jue',
            '媚心术': 'mei_xin_shu',
            '痴情咒': 'chi_qing_zhou',
            '真源法': 'zhen_yuan_fa',
            '玉女素心': 'yu_nv_su_xin',
            '阴阳合欢': 'yin_yang_he_huan',
            '六欲练心': 'liu_yu_lian_xin',
            '颠凤培元': 'dian_feng_pei_yuan',
            '玄月化阴': 'xuan_yue_hua_yin',
            '缠玉绵情': 'chan_yu_mian_qing',
            '七星舞月': 'qi_xing_wu_yue',
            '琅华照烟': 'lang_hua_zhao_yan',
            '霓裳天舞': 'ni_chang_tian_wu',
            '魂牵梦萦': 'hun_qian_meng_ying',
            '缘梦七夕': 'yuan_meng_qi_xi',
            '百花烟雨': 'bai_hua_yan_yu',
            '刹那芳华': 'cha_na_fang_hua',
            '姹女天月': 'cha_nv_tian_yue',
        }
        self.gongfashu = self.gongfashu_name_dict[self.gongfashu_name]
        # self.main_region_coords = self.shuangxiu_coords_manager.main_region_coords

    @wait_region
    def get_mi_shu_coords(self, wait_time, target_region, is_to_click, click_wait_time, to_raise_exception):
        return get_region_coords(
            'mi_shu',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir='shuangxiu'
        )
    
    @wait_region
    def get_shuang_ren_coords(self, wait_time, target_region, is_to_click, click_wait_time, to_raise_exception):
        return get_region_coords(
            'shuang_ren',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir='shuangxiu'
        )

    def click_shuangxiu_gongfashu(self):
        # 在日常界面中，点击双修图标
        gongfashu_coords = get_region_coords(
            self.gongfashu,
            main_region_coords=self.main_region_coords, 
            confidence=0.9, 
            cat_dir='shuangxiu'
        )
        print(f"完成: 识别一次{self.gongfashu_name}位置")

        if gongfashu_coords is None:
            raise Exception(f"未找到{self.gongfashu_name}位置")

        click_region(gongfashu_coords, seconds=3)
        print(f"完成: 点击{self.gongfashu_name}按钮")

    def confirm_yaoqing_daoyou_is_exist(self):
        for yaoqing_daoyou in ['yaoqing_daoyou1', 'yaoqing_daoyou2']:
            yaoqing_daoyou_coords = get_region_coords(
                yaoqing_daoyou, 
                main_region_coords=self.main_region_coords, 
                confidence=0.8, 
                cat_dir='shuangxiu'
            )
            if yaoqing_daoyou_coords is not None:
                return True, yaoqing_daoyou_coords
            
        return False, None

    def click_yaoqing_daoyou(self):
        # 在双修界面中，点击邀请道友按钮
        yaoqing_daoyou_is_exist, yaoqing_daoyou_coords = self.confirm_yaoqing_daoyou_is_exist()
        
        if yaoqing_daoyou_is_exist is False:
            raise Exception("未找到邀请道友按钮")
        
        click_region(yaoqing_daoyou_coords, seconds=4)
        print("完成: 点击邀请道友按钮")

    def go_to_xianyuan_page(self):
        # 前往仙缘界面
        xianyuan_page_coords = self.shuangxiu_coords_manager.xianyuan_page()
        click_region(xianyuan_page_coords, seconds=3)
        print("完成: 前往仙缘界面")

    def click_yaoqing(self):
        # 在仙缘邀请界面中，点击邀请按钮
        yaoqing_region_coords = self.shuangxiu_coords_manager.yaoqing_region()
        args = {
            'target_region_image':'yaoqing', 
            'main_region_coords': yaoqing_region_coords, 
            'confidence': 0.9, 
            'grayscale': True,
            'cat_dir': 'shuangxiu'
        }

        # scroll_length = self.calculate_scroll_length(600)
        while get_region_coords(**args) is None:
            # scroll_specific_length(length=scroll_length)
            scroll_specific_length(
                start_x=0.5,
                end_x=0.5,
                start_y=0.66,
                end_y=0.33,
                seconds=3,
            )

        yaoqing_coords = get_region_coords(**args)
        click_region(yaoqing_coords, seconds=3)
    
    def confirm_go_to_xiulian_is_exist(self):
        go_to_xiulian_coords = get_region_coords(
            'go_to_xiulian',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir='shuangxiu'
        )
        if go_to_xiulian_coords is None:
            return False
        else:
            return True
    
    @wait_region
    def confirm_shuangxiu_is_over(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'shuangxiu_over_indicator',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir='shuangxiu'
        )

    def click_go_to_xiulian(self):
        # 在双修界面中，点击前往修炼按钮
        go_to_xiulian_coords = self.shuangxiu_coords_manager.go_to_xiulian()
        click_region(go_to_xiulian_coords, seconds=4)
        print("完成: 点击前往修炼按钮")

    def speed_up_shuangxiu(self):
        # 在双修界面中，点击屏幕中心, 可以快速跳过双修动画
        start_time = time.time()
        while self.confirm_go_to_xiulian_is_exist() is False:
            if time.time() - start_time > 60:
                raise ShuangXiuException("双修超时")
            
            click_region(self.shuangxiu_coords_manager.main_region_coords, seconds=2)
            print("完成: 点击屏幕中心")
        
        time.sleep(4)

    def scroll_to_top(self, scroll_seconds, scroll_times=5):
        # pyautogui.moveTo(scroll_start_point_coords)
        # scroll_length = self.calculate_scroll_length(scroll_length)
        for _ in range(scroll_times):
            # scroll_specific_length(scroll_length * self.coords_manager.y_ratio, scroll_seconds)
            # scroll_specific_length(scroll_length, scroll_seconds)
            scroll_specific_length(
                start_x=0.5,
                end_x=0.5,
                start_y=0.6,
                end_y=0.8,
                seconds=scroll_seconds,
            )

    def execute(self):
        self.go_to_world()

        # self.click_ri_chang()
        # self.scroll_and_click(direction='down')

        self.get_gong_fa_shu_icon_coords(wait_time=3, target_region='功法书图标', is_to_click=True, click_wait_time=3, to_raise_exception=True)

        self.get_mi_shu_coords(wait_time=3, target_region='秘术', is_to_click=True, click_wait_time=3, to_raise_exception=True)

        self.get_shuang_ren_coords(wait_time=3, target_region='双人', is_to_click=True, click_wait_time=3, to_raise_exception=True)

        self.scroll_to_top(scroll_seconds=2, scroll_times=5)

        self.scroll_and_click(
            direction='down', 
            other_target=self.gongfashu, 
            other_target_name=self.gongfashu_name,
            scroll_seconds=2,
            confidence=0.7
        )
        self.click_yaoqing_daoyou()
        self.go_to_xianyuan_page()
        self.click_yaoqing()

        while True:
            self.click_go_to_xiulian()
            confirm_shuangxiu_is_over_coords = self.confirm_shuangxiu_is_over(
                wait_time=3,
                target_region='双修结束',
                is_to_click=False,
                to_raise_exception=False
            )
            if confirm_shuangxiu_is_over_coords:
                print("完成: 双修结束")
                break

            self.speed_up_shuangxiu()
            self.click_yaoqing_daoyou()
            self.go_to_xianyuan_page()
            self.click_yaoqing()
        
        print("完成: 双修结束!")
        click_region(self.shuangxiu_coords_manager.better_exit())

if __name__ == '__main__':

    # main_region_coords = get_game_page_coords()
    
    coords_manager = ShuangXiuCoordsManager(main_region_coords, resolution=resolution)
    
    sx_executor = ShuangXiuExecutor(coords_manager, gongfashu_name='阴阳合欢')

    sx_executor.execute()