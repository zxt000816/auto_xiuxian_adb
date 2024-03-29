import time
import pyautogui
from utils_adb import *
from coords_manager import BaseCoordsManager
from event_executor import BaseExecutor
from xiuxian_exception import *

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

class GameControlCoordsManager(BaseCoordsManager):
    def __init__(self, main_region_coords, resolution=(1080, 1920)):
        super().__init__(main_region_coords, resolution)
    
    def menu_expansion(self):
        diff = (976, 1743, 52, 54)
        return self.calculate_relative_coords(diff)

    def confirm_in_exit_login_alert(self):
        diff = (582, 1223, 305, 103)
        return self.calculate_relative_coords(diff)
    
    def account_region(self):
        diff = (92, 802, 901, 148)
        return self.calculate_relative_coords(diff)
    
    def scroll_account_ls(self):
        diff = (534, 1044, 0, 0)
        return self.calculate_relative_coords(diff)
    
    def wei_mian(self):
        diff = (401, 1373, 175, 55)
        return self.calculate_relative_coords(diff)

class GameControlExecutor(BaseExecutor):
    def __init__(self, cc_coords_manager: GameControlCoordsManager, account_name: str, account: str, server: str):
        super().__init__(cc_coords_manager, 'game_control')
        self.cc_coords_manager = cc_coords_manager
        self.account_name = account_name
        self.account = account
        self.server_name_dict = {
            '破界飞升': 'po_jie_fei_sheng',
            '黄河入海': 'huang_he_ru_hai',
            '仙山古峪': 'xian_shan_gu_yu',
        }
        self.server = self.server_name_dict[server]

    @wait_region
    def get_menu_expansion_coords(self, wait_time, target_region, is_to_click, click_wait_time):
        menu_expansion_imgs = [
            {'target_region_image': 'menu_expansion1', 'main_region_coords': self.main_region_coords, 'confidence': 0.6, 'grayscale': True, 'cat_dir': 'game_control'},
            {'target_region_image': 'menu_expansion2', 'main_region_coords': self.main_region_coords, 'confidence': 0.6, 'grayscale': True, 'cat_dir': 'game_control'},
            {'target_region_image': 'menu_expansion3', 'main_region_coords': self.main_region_coords, 'confidence': 0.6, 'grayscale': True, 'cat_dir': 'game_control'},
        ]
        return get_region_coords_by_multi_imgs(menu_expansion_imgs)
    
    @wait_region
    def get_setting_coords(self, wait_time, target_region, is_to_click, click_wait_time):
        return get_region_coords(
            'setting',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_exit_login_coords(self, wait_time, target_region, is_to_click, click_wait_time):
        return get_region_coords(
            'exit_login',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_exit_login_alert_coords(self, wait_time, target_region, is_to_click, click_wait_time, other_region_coords):
        return get_region_coords(
            'exit_login_alert',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_login_button_coords(self, wait_time, target_region, is_to_click, click_wait_time, other_region_coords):
        return get_region_coords(
            'login_button',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )

    def scroll_to_top(self, scroll_start_point_coords, scroll_length, scroll_seconds, scroll_times=5):
        for _ in range(scroll_times):
            scroll_specific_length(
                start_x=0.5,
                end_x=0.5,
                start_y=0.6,
                end_y=0.8,
                seconds=scroll_seconds,
            )

    @wait_region
    def get_login_successfully_coords(self, wait_time, target_region, is_to_click, other_region_coords):
        return get_region_coords(
            'login_successfully',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_start_game_coords(self, wait_time, target_region, is_to_click):
        return get_region_coords(
            'start_game',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_wei_mian_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            self.server,
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_select_wei_mian_coords(self, wait_time, target_region, is_to_click, to_raise_exception):
        return get_region_coords(
            f'select_{self.server}',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )

    @wait_region
    def get_vip_fu_li_coords(self, wait_time, target_region, is_to_click, other_region_coords, wait_time_before_click, to_raise_exception):
        return get_region_coords(
            'vip_fu_li',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    @wait_region
    def get_restart_game_coords(self, wait_time, target_region, is_to_click, other_region_coords, to_raise_exception):
        return get_region_coords(
            'restart_game',
            self.main_region_coords,
            confidence=0.7,
            cat_dir=self.cat_dir
        )
    
    def hide_yang_chong_tou(self):
        
        yang_chong_tou_imgs = [
            {'target_region_image': 'yang_chong_tou1', 'main_region_coords': self.main_region_coords, 'confidence': 0.7, 'grayscale': False},
            {'target_region_image': 'yang_chong_tou2', 'main_region_coords': self.main_region_coords, 'confidence': 0.7, 'grayscale': False},
        ]

        yang_chong_tou_coords = get_region_coords_by_multi_imgs(yang_chong_tou_imgs)
        if yang_chong_tou_coords is None:
            return
        
        drag_from_coords = calculate_center_coords(yang_chong_tou_coords)
        drag_to_coords = self.cc_coords_manager.yang_chong_tou_hidden()[:2]

        # pyautogui.moveTo(yang_chong_tou_center_coords[0], yang_chong_tou_center_coords[1])
        # pyautogui.dragTo(hidden_region_coords, duration=2) 
        # time.sleep(2)

        (start_x, start_y) = self.cal_x_y_ratio(drag_from_coords[0], drag_from_coords[1])
        (end_x, end_y) = self.cal_x_y_ratio(drag_to_coords[0], drag_to_coords[1])
        
        scroll_specific_length(start_x, start_x, start_y, start_y, seconds=1)
        scroll_specific_length(start_x, end_x, start_y, end_y, seconds=2)

        confirm_hide_yang_chong_tou_coords = get_region_coords(
            'confirm_hide_yang_chong_tou',
            self.main_region_coords,
            confidence=0.7,
        )
        click_region(confirm_hide_yang_chong_tou_coords)
    
    def exit_current_account(self):
        self.go_to_world()
        # 点击展开菜单
        click_region(self.cc_coords_manager.menu_expansion(), seconds=1)
        # 点击设置
        self.get_setting_coords(wait_time=5, target_region="设置", is_to_click=True, click_wait_time=1)
        # 点击退出登录
        self.get_exit_login_coords(wait_time=5, target_region="退出登录", is_to_click=True, click_wait_time=1)
        # 确认是否弹出退出登录确认框, 如果弹出, 则点击确认
        self.get_exit_login_alert_coords(
            wait_time=5, target_region="退出登录确认框", is_to_click=True, click_wait_time=1, 
            other_region_coords=self.cc_coords_manager.confirm_in_exit_login_alert()
        )

    def execute(self, restart_game=False):

        if restart_game is False:
            self.exit_current_account()

            # 如果检测到登录按钮, 则点击账户区域
            self.get_login_button_coords(
                wait_time=5, target_region="登录按钮", is_to_click=True, click_wait_time=1, 
                other_region_coords=self.cc_coords_manager.account_region()
            )
            # 滚动到顶部
            self.scroll_to_top(
                scroll_start_point_coords=self.cc_coords_manager.scroll_account_ls()[:2],
                scroll_length=1000,
                scroll_seconds=2,
            )
            # 滚动账户列表, 点击指定账户
            self.scroll_and_click(
                direction='down',
                other_target=self.account,
                other_target_name=self.account_name,
                # confidence=0.9,
                confidence=0.8,
                cat_dir='users',
                start_x=0.5,
                end_x=0.5,
                start_y=0.6,
                end_y=0.5,
                scroll_seconds=2,
                scroll_start_point_coords=self.cc_coords_manager.scroll_account_ls()[:2],
                is_to_click=True,
                in_ri_chang_page=False,
            )

            # 点击登录按钮
            self.get_login_button_coords(
                wait_time=5, target_region="登录按钮", is_to_click=True, click_wait_time=1,
                other_region_coords=None 
            )

        # 判断是否弹出vip福利, 如果弹出, 则点击关闭
        self.get_vip_fu_li_coords(
            wait_time=10, target_region="vip福利", is_to_click=True, 
            other_region_coords=self.cc_coords_manager.close_vip_fu_li(), 
            wait_time_before_click=3, to_raise_exception=False
        )

        # 等待登录成功
        self.get_login_successfully_coords(
            wait_time=15, target_region="登录成功", is_to_click=True, 
            other_region_coords=self.cc_coords_manager.exit()
        )

        # 检查是否是指定的位面
        wei_mian_coords = self.get_wei_mian_coords(
            wait_time=10, 
            target_region=self.server, 
            is_to_click=False, 
            to_raise_exception=False
        )

        # 如果不是指定的位面, 则点击选择位面
        if wei_mian_coords is None:
            click_region(self.cc_coords_manager.wei_mian(), seconds=5)
            # 点击选择位面
            self.get_select_wei_mian_coords(wait_time=10, target_region=f"选择{self.server}", is_to_click=True, to_raise_exception=True)

        # 点击开始游戏
        self.get_start_game_coords(wait_time=15, target_region="开始游戏", is_to_click=True)

        restart_game_coords = self.get_restart_game_coords(
            wait_time=2, target_region="重新开始游戏", is_to_click=True, 
            other_region_coords=self.cc_coords_manager.confirm_button_in_restart_game(), to_raise_exception=False
        )
        if restart_game_coords is not None:
            # 如果弹出重新开始游戏, 则点击确认, 然后重新执行
            print("等待游戏重新开始...")
            time.sleep(60)
            return self.execute(restart_game=True)

        self.check_if_specifical_event(
            wait_time=5,
            target_region="是否弹出特殊活动",
            is_to_click=True,
            other_region_coords=self.cc_coords_manager.close_specifical_event(),
            to_raise_exception=False
        )

        # 隐藏洋葱头
        self.hide_yang_chong_tou()

if __name__ == "__main__":
    resolution = (1080, 1920) # (width, height): (554, 984) or (1080, 1920)

    main_region_coords = get_game_page_coords(resolution = resolution)

    coords_manager = GameControlCoordsManager(main_region_coords)

    executor = GameControlExecutor(
        coords_manager, 
        account_name='白起(仙山)', 
        account='17633025505',
        server='仙山古峪'
    )
    executor.execute()
