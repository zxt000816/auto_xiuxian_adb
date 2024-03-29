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
from utils_adb import get_game_page_coords, get_region_coords, click_region, wait_region, get_region_coords_by_multi_imgs, calculate_center_coords, click_if_coords_exist, scroll_specific_length
from coords_manager import BaseCoordsManager
from event_executor import BaseExecutor
from xiuxian_exception import ScrollException

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

class XiuLianCoordsManager(BaseCoordsManager):
    def __init__(self, main_region_coords, resolution=(1080, 1920)):
        super().__init__(main_region_coords, resolution)

    def xiu_lian_small(self):
        diff = (81, 1584, 252, 277)
        return self.calculate_relative_coords(diff)
    
    def xiu_lian_left_arrow(self):
        diff = (67, 1431, 52, 100)
        return self.calculate_relative_coords(diff)
    
    def check_upgrade_gong_fa_shu_button(self):
        diff = (839, 1744, 116, 112)
        return self.calculate_relative_coords(diff)
    
    def jing_yan_shu_list(self):
        diff = (330, 1094, 470, 504)
        return self.calculate_relative_coords(diff)
    
    def confirm_button_in_yi_chu_alert(self):
        diff = (401, 1224, 304, 99)
        return self.calculate_relative_coords(diff)
    
    def jing_yan_store_scroll_start_point(self):
        diff = (562, 1328, 0, 0)
        return self.calculate_relative_coords(diff)
    
    def wait_detect_mouse_pos(self):
        diff = (211, 307, 0, 0)
        return self.calculate_relative_coords(diff)
    
    def switch_gong_fa_icon(self):
        diff = (854, 1606, 85, 102)
        return self.calculate_relative_coords(diff)

    def switch_gong_fa(self):
        diff = (423, 883, 216, 51)
        return self.calculate_relative_coords(diff)
    
    def ti_sheng_icon(self):
        diff = (855, 1753, 77, 85)
        return self.calculate_relative_coords(diff)
        
class XiuLianExecutor(BaseExecutor):
    def __init__(self, xl_coords_manager: XiuLianCoordsManager, buy_times):
        super().__init__(xl_coords_manager, 'xiu_lian')
        self.xl_coords_manager = xl_coords_manager
        self.buy_times = buy_times

    @wait_region    
    def get_xiu_lian_icon_coords(self, wait_time, target_region, is_to_click):
        click_region(self.xl_coords_manager.xiu_lian_left_arrow(), seconds=1)
        return get_region_coords(
            'xiu_lian_icon',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )

    @wait_region
    def get_fu_yong_over_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'fu_yong_over',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    @click_if_coords_exist
    def get_ti_sheng_coords(self, target_region, to_raise_exception):
        return get_region_coords(
            'ti_sheng',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_xiu_lian_xin_de_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'xiu_lian_xin_de',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_jing_yan_shu_coords(self, wait_time, target_region, is_to_click, to_raise_exception):

        check_region = self.xl_coords_manager.jing_yan_shu_list()

        xiu_lian_imgs = [
            {'target_region_image': 'qian_xiu_zhen_wu', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
            {'target_region_image': 'qian_xiu_xin_de_si_ke', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
            {'target_region_image': 'qian_xiu_xin_de_yi_shi', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
            {'target_region_image': 'gong_fa_wu_jie', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
            {'target_region_image': 'gong_fa_si_jie', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
            {'target_region_image': 'gong_fa_san_jie', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
            {'target_region_image': 'gong_fa_er_jie', 'main_region_coords': check_region, 'confidence': 0.7, 'grayscale': False, 'cat_dir': 'xiu_lian'},
        ]
        return get_region_coords_by_multi_imgs(xiu_lian_imgs)
    
    @wait_region
    def get_upgrade_gong_fa1_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'upgrade_gong_fa1',
            main_region_coords=self.xl_coords_manager.check_upgrade_gong_fa_shu_button(),
            confidence=0.9,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_xiao_lv_ping_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'xiao_lv_ping',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )

    @wait_region
    def get_upgrade_gong_fa2_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'upgrade_gong_fa2',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_upgrade_gong_fa3_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'upgrade_gong_fa3',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_click_screen_continue_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'click_screen_continue',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_xiu_lian_button_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'xiu_lian_button',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_xiu_lian_button_in_switch_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'xiu_lian_button_in_switch',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )

    @wait_region
    def get_yi_chu_alert_coords(self, wait_time, target_region, is_to_click, other_region_coords, to_raise_exception):
        return get_region_coords(
            'yi_chu_alert',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    def switch_gong_fa(self):

        click_region(self.xl_coords_manager.switch_gong_fa_icon(), seconds=2)
        click_region(self.xl_coords_manager.switch_gong_fa_icon(), seconds=2)
        click_region(self.xl_coords_manager.switch_gong_fa_icon(), seconds=2)
        click_region(self.xl_coords_manager.switch_gong_fa(), seconds=2)

        self.get_xiu_lian_button_in_switch_coords(
            wait_time=3,
            target_region='修炼按钮',
            is_to_click=True,
            to_raise_exception=True,
        )

        time.sleep(3)
    
    def process_alert_in_level_up(self):

        gong_fa_max_level_coords = self.get_gong_fa_max_level_coords(
            wait_time=2,
            target_region='功法满级',
            is_to_click=False,
            to_raise_exception=False,
        )
        if gong_fa_max_level_coords is not None:
            self.switch_gong_fa()
            return True

        # 如果弹出了经验溢出提示，点击确认, 然后执行提升
        self.get_yi_chu_alert_coords(
            wait_time=3,
            target_region='经验溢出提示',
            is_to_click=True,
            other_region_coords=self.xl_coords_manager.confirm_button_in_yi_chu_alert(),
            to_raise_exception=False,
        )
        
        # 如果没有弹出经验溢出提示，但是弹出了提升箭头，点击提升箭头
        gong_fa1_coords = self.get_upgrade_gong_fa1_coords(
            wait_time=3, 
            target_region='提升1', 
            is_to_click=False, 
            to_raise_exception=False
        )

        if gong_fa1_coords is not None:
            print("检测到功法书可以提升!")
            pyautogui.mouseUp()

            time.sleep(3)
            click_region(gong_fa1_coords, seconds=2)

            self.get_upgrade_gong_fa2_coords(wait_time=3, target_region='提升2', is_to_click=True, to_raise_exception=False)
            self.get_upgrade_gong_fa3_coords(wait_time=3, target_region='提升3', is_to_click=True, to_raise_exception=False)
            self.get_click_screen_continue_coords(wait_time=3, target_region='屏幕继续', is_to_click=True, to_raise_exception=False)
            xiu_lian_button_coords = self.get_xiu_lian_button_coords(wait_time=3, target_region='修炼按钮', is_to_click=False, to_raise_exception=False)
            if xiu_lian_button_coords :
                click_region(self.xl_coords_manager.exit(), seconds=2)
            
            self.get_ti_sheng_coords(target_region='提升', to_raise_exception=False)
            return True

        return False

    def xiu_lian_xin_de_level_up(self):
        # 移动到修炼心得
        xiu_lian_xin_de_coords = self.get_xiu_lian_xin_de_coords(wait_time=2, target_region='修炼心得', is_to_click=False, to_raise_exception=False)
        if xiu_lian_xin_de_coords is None:
            click_region(self.xl_coords_manager.ti_sheng_icon())
        
        xiu_lian_xin_de_coords = self.get_xiu_lian_xin_de_coords(wait_time=2, target_region='修炼心得', is_to_click=False, to_raise_exception=False)
        xiu_lian_xin_de_center = calculate_center_coords(xiu_lian_xin_de_coords)
        pyautogui.moveTo(xiu_lian_xin_de_center, duration=0.5)

    def gong_fa_shu_level_up(self):
        xiu_lian_xin_de_coords = self.get_xiu_lian_xin_de_coords(wait_time=2, target_region='修炼心得', is_to_click=False, to_raise_exception=False)
        if xiu_lian_xin_de_coords is None:
            click_region(self.xl_coords_manager.ti_sheng_icon())
        
        jing_yan_shu_coords = self.get_jing_yan_shu_coords(wait_time=2, target_region='经验书', is_to_click=False, to_raise_exception=False)
        if jing_yan_shu_coords is None:
            print("没有经验书!")
            return None
        
        jing_yan_shu_center = calculate_center_coords(jing_yan_shu_coords)
        pyautogui.moveTo(jing_yan_shu_center, duration=0.5)
        return jing_yan_shu_coords

    @wait_region
    def get_store_open_indicator_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'store_open_indicator',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_zero_xiu_lian_xin_de_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'zero_xiu_lian_xin_de',
            main_region_coords=self.main_region_coords,
            confidence=0.8,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_chang_an_alert_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'chang_an_alert',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    @wait_region
    def get_gong_fa_max_level_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            'gong_fa_max_level',
            main_region_coords=self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir,
        )
    
    def execute(self):

        self.go_to_world()

        # 进入修炼
        click_region(self.xl_coords_manager.xiu_lian_small(), seconds=5)
        # 寻找并点击修炼图标
        self.get_xiu_lian_icon_coords(wait_time=15, target_region='修炼图标', is_to_click=True)
        # 检查是否弹出了丹药服用结束的窗口
        fu_yong_over_coords = self.get_fu_yong_over_coords(wait_time=2, target_region='服用结束', is_to_click=False, to_raise_exception=False)
        if fu_yong_over_coords is not None:
            print('完成: 弹出了丹药服用结束的窗口，点击退出!')
            click_region(self.xl_coords_manager.exit())
        
        # 点击提升按钮
        self.get_ti_sheng_coords(target_region='提升', to_raise_exception=True)

        if self.buy_times > 0:
            try:
                self.scroll_and_click(
                    direction='down',
                    other_target='buy_qian_xiu_zhen_wu',
                    other_target_name='潜修真悟',
                    confidence=0.7,
                    start_x=0.5,
                    end_x=0.5,
                    start_y=0.75,
                    end_y=0.6,
                    num_of_scroll=4,
                    scroll_seconds=2,
                    cat_dir='xiu_lian',
                    in_ri_chang_page=False,
                    is_to_click=True,
                )

                store_open_indicator_args = { 'wait_time': 3, 'target_region': '商店打开标志', 'is_to_click': False, 'to_raise_exception': False }
                if self.get_store_open_indicator_coords(**store_open_indicator_args) is not None:
                    actual_buy_times = self.buy_times_in_store(self.buy_times)
                    print(f"实际购买次数: {actual_buy_times}")
                    if self.get_store_open_indicator_coords(**store_open_indicator_args) is None:
                        self.get_ti_sheng_coords(target_region='提升', to_raise_exception=True)
                    else:
                        click_region(self.xl_coords_manager.exit())
                else:
                    print("商店未打开, 无法购买!")

            except ScrollException:
                print("未找到可购买的潜修真悟!")

        xiu_lian_xin_de_coords = self.get_xiu_lian_xin_de_coords(wait_time=2, target_region='修炼心得', is_to_click=False, to_raise_exception=False)
        if xiu_lian_xin_de_coords is None:
            click_region(self.xl_coords_manager.ti_sheng_icon())

        start_time = time.time()
        while True:
            # 检查是否到达120秒
            if time.time() - start_time > 120:
                print("到达120秒,退出!")
                break

            xiu_lian_xin_de_coords = self.get_xiu_lian_xin_de_coords(
                wait_time=2, 
                target_region='修炼心得', 
                is_to_click=False, 
                to_raise_exception=False
            )
            if xiu_lian_xin_de_coords is not None:
                self.press(xiu_lian_xin_de_coords, seconds=2, duration=10)

            alert_is_existed = self.process_alert_in_level_up()
            if alert_is_existed is False:
                print("未检测到弹窗, 修炼心得使用完毕!")
                break
        
        xiu_lian_xin_de_coords = self.get_xiu_lian_xin_de_coords(wait_time=2, target_region='修炼心得', is_to_click=False, to_raise_exception=False)
        if xiu_lian_xin_de_coords is None:
            click_region(self.xl_coords_manager.ti_sheng_icon())

        start_time = time.time()
        while True:
            # 检查是否到达240秒
            if time.time() - start_time > 240:
                print("到达240秒,退出!")
                break

            jing_yan_shu_coords = self.get_jing_yan_shu_coords(
                wait_time=2, 
                target_region='经验书',
                is_to_click=False, 
                to_raise_exception=False
            )
            if jing_yan_shu_coords is not None:
                self.press(jing_yan_shu_coords, seconds=2, duration=10)
            else:
                print("没有经验书!")
                break

            alert_is_existed = self.process_alert_in_level_up()
        
        # 使用小绿瓶
        self.get_xiao_lv_ping_coords(wait_time=2, target_region='小绿瓶', is_to_click=True, to_raise_exception=False)

        time.sleep(3)
        click_region(self.xl_coords_manager.better_exit(), seconds=2)

    def old_execute(self):
        self.go_to_world()

        # 进入修炼
        click_region(self.xl_coords_manager.xiu_lian_small(), seconds=5)
        # 寻找并点击修炼图标
        self.get_xiu_lian_icon_coords(wait_time=15, target_region='修炼图标', is_to_click=True)
        # 检查是否弹出了丹药服用结束的窗口
        fu_yong_over_coords = self.get_fu_yong_over_coords(wait_time=2, target_region='服用结束', is_to_click=False, to_raise_exception=False)
        if fu_yong_over_coords is not None:
            print('完成: 弹出了丹药服用结束的窗口，点击退出!')
            click_region(self.xl_coords_manager.exit())
        
        # 点击提升按钮
        self.get_ti_sheng_coords(target_region='提升', to_raise_exception=True)

        if self.buy_times > 0:
            try:
                self.scroll_and_click(
                    direction='down',
                    other_target='buy_qian_xiu_zhen_wu',
                    other_target_name='潜修真悟',
                    confidence=0.7,
                    num_of_scroll=4,
                    scroll_seconds=3,
                    grayscale=False,
                    scroll_start_point_coords=self.xl_coords_manager.jing_yan_store_scroll_start_point()[:2],
                    cat_dir='xiu_lian',
                    in_ri_chang_page=False,
                    is_to_click=True,
                )

                store_open_indicator_args = { 'wait_time': 3, 'target_region': '商店打开标志', 'is_to_click': False, 'to_raise_exception': False }
                if self.get_store_open_indicator_coords(**store_open_indicator_args) is not None:
                    actual_buy_times = self.buy_times_in_store(self.buy_times)
                    print(f"实际购买次数: {actual_buy_times}")
                    if self.get_store_open_indicator_coords(**store_open_indicator_args) is None:
                        self.get_ti_sheng_coords(target_region='提升', to_raise_exception=True)
                    else:
                        click_region(self.xl_coords_manager.exit())
                else:
                    print("商店未打开, 无法购买!")

            except ScrollException:
                print("未找到可购买的潜修真悟!")

        #如果没有看到修炼心得，就再次点击提升
        chang_an_alert_coords = self.get_chang_an_alert_coords(wait_time=2, target_region='长按提示', is_to_click=False, to_raise_exception=False)
        if chang_an_alert_coords is None:
            self.get_ti_sheng_coords(target_region='提升', to_raise_exception=True)

        #滚动会顶部
        scroll_length = self.calculate_scroll_length(1000)
        for _ in range(3):
            print("滚动到顶部!")
            pyautogui.moveTo(self.xl_coords_manager.jing_yan_store_scroll_start_point()[:2])
            # scroll_specific_length(scroll_length, seconds=1)
            scroll_specific_length(
                start_x=0.5,
                end_x=0.5,
                start_y=0.33,
                end_y=0.66,
                seconds=1,
            )

        self.xiu_lian_xin_de_level_up()
        pyautogui.mouseDown()

        start_time = time.time()
        total_time = 20
        while True:
            # 检查是否到达20秒
            if time.time() - start_time > total_time:
                print("到达20秒,退出!")
                pyautogui.mouseUp()
                break

            # 处理弹出的窗口
            if_processed = self.process_alert_in_level_up()
            if if_processed is True:
                # 如果处理了弹出的窗口，就将计时器重置
                self.xiu_lian_xin_de_level_up()
                pyautogui.mouseDown()
                start_time = time.time()
            
            zero_xiu_lian_xin_de_coords = self.get_zero_xiu_lian_xin_de_coords(
                wait_time=2, target_region='修炼心得为0', 
                is_to_click=False, to_raise_exception=False
            )
            if zero_xiu_lian_xin_de_coords is not None:
                print("修炼心得为0，退出!")
                pyautogui.mouseUp()
                break

        ############################################################################################################
        self.gong_fa_shu_level_up()
        pyautogui.mouseDown()

        start_time = time.time()
        total_time = 10
        while True:
            # 检查是否到达20秒
            if time.time() - start_time > total_time:
                pyautogui.mouseUp()
                pyautogui.moveTo(self.xl_coords_manager.wait_detect_mouse_pos()[:2])
                if self.gong_fa_shu_level_up() is None:
                    print("到达5秒，退出!")
                    break
                else:
                    pyautogui.mouseDown()
                    start_time = time.time()
                    continue

            # 处理弹出的窗口
            if_processed = self.process_alert_in_level_up()
            if if_processed is True:
                # 如果处理了弹出的窗口，就将计时器重置
                self.gong_fa_shu_level_up()
                pyautogui.mouseDown()
                start_time = time.time()

        # 使用小绿瓶
        self.get_xiao_lv_ping_coords(wait_time=2, target_region='小绿瓶', is_to_click=True, to_raise_exception=False)

if __name__ == '__main__':
    
    # resolution = (1080, 1920) # (width, height): (554, 984) or (1080, 1920)

    # main_region_coords = get_game_page_coords(resolution = resolution)

    coords_manager = XiuLianCoordsManager(main_region_coords, resolution=resolution)
    executor = XiuLianExecutor(coords_manager, buy_times=1)

    executor.execute()
