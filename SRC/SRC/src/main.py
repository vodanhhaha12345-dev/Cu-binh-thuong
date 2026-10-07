import flet as ft
import random
import asyncio


def main(page: ft.Page):
    page.title = "CỨ BÌNH THƯỜNG"
    page.bgcolor = "#0a0c12"
    page.padding = 15
    page.window.width = 360
    page.window.height = 640

    NUT_TOI = "#282d3c"
    NUT_SANG = "#00dcb4"
    CHU_TRANG = "#ffffff"
    CHU_MO = "#788296"
    CHU_DO = "#ff5050"
    CHU_VANG = "#ffcc00"
    NEN_CHAM_NGON = "#141a26"

    # State chuyển ra ngoài để giữ khi qua lại màn
    game_state = {
        "so": 0,
        "nut_sang": random.randint(0, 4),
        "ky_luc": 0,
        "cau": "Bạn không cần phải nói gì cả.",
    }

    CAU = [
        "Bạn không cần phải nói gì cả.",
        "Đám đông sẽ qua thôi.",
        "Thở một cái.",
        "30 giây nữa thôi.",
        "Bạn ổn mà.",
        "Không ai để ý bạn đâu.",
        "Cứ bấm tiếp đi.",
        "Cẩn thận. Bấm sai là mất hết.",
    ]

    def xoa():
        page.controls.clear()

    async def delay_hien_nut(nut):
        await asyncio.sleep(4)
        nut.visible = True
        page.update()

    # ============================================================
    # MÀN 1: HƯỚNG DẪN
    # ============================================================
    def man_huong_dan():
        xoa()

        tieu_de = ft.Text("📖 HƯỚNG DẪN",
                          size=22, weight=ft.FontWeight.BOLD,
                          color=CHU_TRANG, text_align=ft.TextAlign.CENTER)

        muc_dich = ft.Text(
            "Dành cho khoảnh khắc ngại ngùng ngắn — khi bạn đứng "
            "chờ thang máy đông, đi ngang qua đám đông, hoặc đợi "
            "xe buýt.\n\n"
            "Lúc đó bạn không biết làm gì với điện thoại — chỉ cần "
            "mở app và bấm.\n\n"
            "Không cần cày. Không cần mục tiêu. Chỉ là công cụ để "
            "bạn vượt qua 30 giây khó xử.",
            size=13, color=CHU_TRANG)

        tom_tat = ft.Text(
            "App này giúp bạn vượt qua 30 giây khi đi qua đám đông "
            "và ngại ngùng, không biết làm gì cả.",
            size=13, color=CHU_TRANG,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER)

        cach_choi = ft.Text(
            "• Bấm nút đang sáng → số tăng.\n"
            "• Bấm sai → số về 0.\n"
            "• Cố gắng đạt số cao nhất.\n"
            "• Không cần cày. Chơi khi cần thôi.",
            size=13, color=CHU_TRANG)

        nut_tiep = ft.Button(
            "TIẾP THEO →",
            on_click=lambda e: man_canh_bao(),
            bgcolor=NUT_SANG, color="#000000",
            width=200, height=45,
            visible=False,
        )

        page.add(
            ft.Column([
                ft.Container(height=20),
                tieu_de,
                ft.Container(height=20),
                ft.Text("MỤC ĐÍCH", size=12,
                        weight=ft.FontWeight.BOLD, color=CHU_VANG),
                ft.Container(height=6),
                muc_dich,
                ft.Container(height=10),
                tom_tat,
                ft.Container(height=20),
                ft.Text("CÁCH CHƠI", size=12,
                        weight=ft.FontWeight.BOLD, color=CHU_VANG),
                ft.Container(height=6),
                cach_choi,
                ft.Container(expand=True),
                ft.Row([nut_tiep], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=15),
            ], expand=True,
               horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               scroll=ft.ScrollMode.AUTO)
        )
        page.update()
        page.run_task(delay_hien_nut, nut_tiep)

    # ============================================================
    # MÀN 2: LƯU Ý CHO NGƯỜI DÙNG
    # ============================================================
    def man_canh_bao():
        xoa()

        tieu_de = ft.Text("⚠️ LƯU Ý CHO NGƯỜI DÙNG",
                          size=22, weight=ft.FontWeight.BOLD,
                          color=CHU_DO, text_align=ft.TextAlign.CENTER)

        noi_dung = ft.Text(
            "App là công cụ giải trí đơn thuần.\n\n"
            "• Không phải thiết bị y tế.\n"
            "• Không chẩn đoán, tư vấn hoặc điều trị bệnh tâm lý.\n"
            "• Không thay thế chuyên gia y tế.\n"
            "• Nếu có dấu hiệu lo âu hoặc trầm cảm, hãy liên hệ "
            "chuyên gia ngay.\n\n"
            "• Không thu thập hoặc chia sẻ dữ liệu cá nhân.\n"
            "• Kỷ lục chỉ lưu cục bộ trên thiết bị của bạn.\n"
            "• Việc sử dụng app là tự nguyện.\n"
            "• Nhà phát triển không chịu trách nhiệm cho bất kỳ "
            "hậu quả nào phát sinh từ việc sử dụng app.\n\n"
            "Bằng cách bấm BẮT ĐẦU, bạn xác nhận đã đọc và đồng ý "
            "với các lưu ý trên.",
            size=12, color=CHU_TRANG, text_align=ft.TextAlign.CENTER)

        nut_bat_dau = ft.Button(
            "BẮT ĐẦU",
            on_click=lambda e: man_game(),
            bgcolor=NUT_SANG, color="#000000",
            width=200, height=45,
            visible=False,
        )

        page.add(
            ft.Column([
                ft.Container(height=20),
                tieu_de,
                ft.Container(height=20),
                noi_dung,
                ft.Container(expand=True),
                ft.Row([nut_bat_dau], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=15),
            ], expand=True,
               horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               scroll=ft.ScrollMode.AUTO)
        )
        page.update()
        page.run_task(delay_hien_nut, nut_bat_dau)

    # ============================================================
    # MÀN 3: GAME
    # ============================================================
    def man_game():
        xoa()

        so_text = ft.Text(str(game_state["so"]), size=48,
                          weight=ft.FontWeight.BOLD, color=CHU_TRANG)
        kl_text = ft.Text(f"Kỷ lục: {game_state['ky_luc']}",
                          size=13, color=CHU_MO)

        # ===== CHÂM NGÔN — NỔI BẬT =====
        cau_text = ft.Text(
            game_state["cau"],
            size=15,
            weight=ft.FontWeight.BOLD,
            color=CHU_VANG,
            text_align=ft.TextAlign.CENTER,
        )

        khung_cham_ngon = ft.Container(
            content=cau_text,
            bgcolor=NEN_CHAM_NGON,
            padding=14,
            border_radius=12,
            width=300,
        )

        luat_text = ft.Text("Bấm nút sáng → +1  |  Bấm sai → về 0",
                            size=11, color=CHU_DO,
                            text_align=ft.TextAlign.CENTER)

        NUT_SIZE = 58
        nut_list = []
        for i in range(5):
            nut_list.append(ft.Container(
                width=NUT_SIZE, height=NUT_SIZE,
                bgcolor=NUT_TOI, border_radius=14,
                on_click=lambda e, idx=i: bam(idx),
            ))

        # ===== NÚT THÔNG TIN — RÕ RÀNG =====
        nut_tt = ft.Button(
            "ℹ️  THÔNG TIN ỨNG DỤNG",
            on_click=lambda e: man_thong_tin(),
            bgcolor="#2a3548",
            color=CHU_TRANG,
            width=240,
            height=45,
        )

        def cap_nhat():
            for i, n in enumerate(nut_list):
                n.bgcolor = NUT_SANG if i == game_state["nut_sang"] else NUT_TOI
            so_text.value = str(game_state["so"])
            kl_text.value = f"Kỷ lục: {game_state['ky_luc']}"
            cau_text.value = game_state["cau"]
            page.update()

        def doi_nut_sang():
            cu = game_state["nut_sang"]
            game_state["nut_sang"] = random.choice([i for i in range(5) if i != cu])

        def bam(idx):
            if idx == game_state["nut_sang"]:
                game_state["so"] += 1
                if game_state["so"] > game_state["ky_luc"]:
                    game_state["ky_luc"] = game_state["so"]
                if game_state["so"] % 10 == 0:
                    game_state["cau"] = random.choice(CAU)
                doi_nut_sang()
            else:
                game_state["so"] = 0
                game_state["cau"] = "Bấm sai! Mất hết rồi."
            cap_nhat()

        hang_tren = ft.Row([nut_list[0], nut_list[1]],
                           alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        hang_giua = ft.Row([nut_list[2]],
                           alignment=ft.MainAxisAlignment.CENTER)
        hang_duoi = ft.Row([nut_list[3], nut_list[4]],
                           alignment=ft.MainAxisAlignment.SPACE_EVENLY)

        page.add(
            ft.Column([
                khung_cham_ngon,
                ft.Container(height=10),
                so_text,
                kl_text,
                ft.Container(height=10),
                hang_tren,
                ft.Container(height=8),
                hang_giua,
                ft.Container(height=8),
                hang_duoi,
                ft.Container(height=12),
                luat_text,
                ft.Container(expand=True),
                ft.Row([nut_tt], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=10),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               spacing=0, expand=True)
        )
        cap_nhat()

    # ============================================================
    # MÀN 4: THÔNG TIN ỨNG DỤNG
    # ============================================================
    def man_thong_tin():
        xoa()

        nut_back = ft.Button(
            "← Quay lại",
            on_click=lambda e: man_game(),
            bgcolor=NUT_SANG, color="#000000",
            width=140, height=42,
        )

        tieu_de = ft.Text("ℹ️ THÔNG TIN ỨNG DỤNG",
                          size=20, weight=ft.FontWeight.BOLD,
                          color=CHU_TRANG, text_align=ft.TextAlign.CENTER)

        gioi_thieu = ft.Text(
            "Cứ Bình Thường là ứng dụng nhỏ giúp bạn có việc làm "
            "trong vài giây khi rơi vào tình huống ngại ngùng — "
            "chờ thang máy, qua đám đông, đợi xe buýt.\n\n"
            "Không phải game để cày. Không có mục tiêu. Chỉ là "
            "công cụ để bạn vượt qua khoảnh khắc khó xử.",
            size=12, color=CHU_TRANG)

        tt = ft.Text(
            "Tên ứng dụng : Cứ Bình Thường\n"
            "Phiên bản    : 1.0\n"
            "Nền tảng     : Android\n"
            "Ngôn ngữ     : Tiếng Việt\n"
            "Giá          : Miễn phí\n"
            "Quảng cáo    : Không có",
            size=12, color=CHU_TRANG)

        pl = ft.Text(
            "• Không phải thiết bị y tế.\n"
            "• Không chẩn đoán, tư vấn hoặc điều trị bệnh tâm lý.\n"
            "• Không thay thế chuyên gia y tế.\n"
            "• Nếu có dấu hiệu lo âu hoặc trầm cảm, hãy liên hệ "
            "chuyên gia ngay.\n"
            "• Không thu thập hoặc chia sẻ dữ liệu cá nhân.\n"
            "• Kỷ lục chỉ lưu cục bộ trên thiết bị.\n"
            "• Việc sử dụng app là tự nguyện.\n"
            "• Nhà phát triển không chịu trách nhiệm cho bất kỳ "
            "hậu quả nào phát sinh từ việc sử dụng app.",
            size=12, color=CHU_TRANG)

        bq = ft.Text(
            "© 2026 — Cứ Bình Thường\n"
            "Mọi quyền được bảo lưu.",
            size=11, color=CHU_MO, text_align=ft.TextAlign.CENTER)

        page.add(
            ft.Column([
                ft.Row([nut_back], alignment=ft.MainAxisAlignment.START),
                ft.Container(height=5),
                tieu_de,
                ft.Container(height=20),
                ft.Text("GIỚI THIỆU", size=12,
                        weight=ft.FontWeight.BOLD, color=CHU_VANG),
                ft.Container(height=6),
                gioi_thieu,
                ft.Container(height=20),
                ft.Text("THÔNG TIN", size=12,
                        weight=ft.FontWeight.BOLD, color=CHU_VANG),
                ft.Container(height=6),
                tt,
                ft.Container(height=20),
                ft.Text("LƯU Ý PHÁP LÝ", size=12,
                        weight=ft.FontWeight.BOLD, color=CHU_DO),
                ft.Container(height=6),
                pl,
                ft.Container(height=20),
                bq,
                ft.Container(height=20),
            ], expand=True,
               horizontal_alignment=ft.CrossAxisAlignment.START,
               scroll=ft.ScrollMode.AUTO)
        )
        page.update()

    man_huong_dan()


ft.run(main)
