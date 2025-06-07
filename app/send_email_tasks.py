from app import database, models, email_utils


from app.tasks import send_reply_email, send_reply_email_with_attachments


db = database.get_db()


# BCD 项目类型发送邮件
def schedule_bid_conversation_BCD(
    b_company: models.CompanyInfo, 
    c_company: models.CompanyInfo, 
    d_company: models.CompanyInfo, 
    contract_serial_number: str,
    project_name: str):

    # smtp_config = {
    #             "host": "smtp.163.com",
    #             "port": 465,
    #            "username": "peterlcylove@163.com",
    #             "password": "ECRVsnXCe2g2Xauq",
    #             "from": "peterlcylove@163.com"
    #         }
    
    b_smtp = {
        "host": "smtp.163.com",
        "port": 465,
        "username": "peterlcylove@163.com",
        "password": "ECRVsnXCe2g2Xauq",
        "from": "peterlcylove@163.com"
    }

    c_smtp = {
        "host": "smtp.qq.com",
        "port": 465,
        "username": "494762262@qq.com",
        "password": "mlnbblbyyvulbhhi",
        "from": "494762262@qq.com"
    }

    d_smtp = {
        "host": "smtp.qq.com",
        "port": 465,
        "username": "494762262@qq.com",
        "password": "mlnbblbyyvulbhhi",
        "from": "494762262@qq.com"
    }

    b_email = b_company.email
    c_email = c_company.email
    d_email = d_company.email

    # 获取对应B公司的邮件模板
    b_email_subject_b3   = email_utils.render_email_subject("B3", b_company.short_name, project_name, contract_serial_number)
    b_email_content_b3 = email_utils.render_invitation_template_content(
        project_name=project_name,
        serial_number="L123456789",
        first_name=c_company.last_name,
        winning_amount="1000000",
        contract_number="HTLS20250606001",
        template_name="B3_"+b_company.short_name+".html"
    )
    
    print("B3-B公司邮件主题：", b_email_subject_b3)
    
    # 第一封邮件：B ➝ C（立即）
    task1 = send_reply_email.apply_async(
        args=[c_email, b_email_subject_b3, b_email_content_b3, b_smtp],
        countdown=0  # 立即
    )

    # 第二封邮件：C ➝ B 回复
    # 随机延迟 5–60 分钟
    c_email_subject_b4 = email_utils.render_email_subject(
        stage="B4", 
        company_short_name=c_company.short_name, 
        project_name=project_name, 
        serial_number="L123456789",
        contract_number="HTLS20250606001",
    )
    
    print("B4-C公司邮件主题：", c_email_subject_b4)
    
    c_email_content_b4 = email_utils.render_invitation_template_content(
        buyer_name=c_company.company_name, 
        project_name=project_name, 
        serial_number="L123456789",
        first_name=b_company.last_name,
        winning_amount="1000000",
        contract_number="HTLS20250606001",
        template_name="B4_"+c_company.short_name+".html")
    
    # delay2 = random.randint(5, 60)
    delay2 =  1
    task2 = send_reply_email.apply_async(
        args=[b_email, c_email_subject_b4, c_email_content_b4, c_smtp],
        countdown=delay2 * 60  # 相对第一封
    )

    # 第三封：B ➝ D（延迟第2封基础上 5–60分钟）
    b_email_subject_b5 = email_utils.render_email_subject(
        stage="B5", 
        company_short_name=b_company.short_name, 
        project_name=project_name, 
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="1000000",
        winning_time="2025-06-06"
    )
    
    print("B5-B公司邮件主题：", b_email_subject_b5)
    
    b_email_content_b5 = email_utils.render_invitation_template_content(
        buyer_name=b_company.company_name, 
        first_name=d_company.last_name,
        winning_amount="1000000",
        contract_number="HTLS20250606001",
        serial_number="L123456789",
        project_name=project_name, 
        winning_time="2025-06-06",
        template_name="B5_"+b_company.short_name+".html"
    )

    # delay3 = delay2 + random.randint(5, 60)
    delay3 = delay2 + 1
    task3 = send_reply_email.apply_async(
        args=[d_email, b_email_subject_b5, b_email_content_b5, b_smtp],
        countdown=delay3 * 60
    )

    # 第四封：D ➝ B（在第3封后延迟 5–60分钟）
    d_email_subject_b6 = email_utils.render_email_subject(
        stage="B6",
        company_short_name=d_company.short_name,
        project_name=project_name,
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="1000000",
        winning_time="2025-06-06"
    )
    
    print("B6-D公司邮件主题：", d_email_subject_b6)
    
    d_email_content_b6 = email_utils.render_invitation_template_content(
        buyer_name=d_company.company_name, 
        first_name=b_company.last_name_traditional,
        winning_amount="1000000",
        contract_number="HTLS20250606001",
        serial_number="L123456789",
        project_name=project_name, 
        winning_time="2025-06-06",
        template_name="B6_"+d_company.short_name+".html"
    )
    # delay4 = delay3 + random.randint(5, 60)
    delay4 = delay3 + 1
    task4 = send_reply_email.apply_async(
        args=[b_email, d_email_subject_b6, d_email_content_b6, d_smtp],
        countdown=delay4 * 60
    )

    # return {
    #     "tasks": [
    #         {"step": "B ➝ C", "task_id": task1.id, "delay_min": 0},
    #         {"step": "C ➝ B", "task_id": task2.id, "delay_min": delay2},
    #         {"step": "B ➝ D", "task_id": task3.id, "delay_min": delay3},
    #         {"step": "D ➝ B", "task_id": task4.id, "delay_min": delay4},
    #     ]
    # }
    return {"message": "email sent!"}


# CCD 项目类型发送邮件
# 仅有BD公司之间发送两封邮件
def schedule_bid_conversation_CCD(
    b_company: models.CompanyInfo, 
    d_company: models.CompanyInfo, 
    contract_serial_number: str,
    project_name: str):


    b_smtp = {
        "host": b_company.smtp_host,
        "port": b_company.smtp_port,
        "username": b_company.smtp_username,
        "password": b_company.smtp_password,
        "from": b_company.smtp_from
    }

    d_smtp = {
        "host": d_company.smtp_host,
        "port": d_company.smtp_port,
        "username": d_company.smtp_username,
        "password": d_company.smtp_password,
        "from": d_company.smtp_from
    }

    b_email = b_company.email
    d_email = d_company.email

    # 获取对应B公司的邮件模板
    b_email_subject_b3   = email_utils.render_email_subject("B3", b_company.short_name, project_name, contract_serial_number)
    b_email_content_b3 = email_utils.render_invitation_template_content(
        project_name=project_name,
        serial_number="L123456789",
        first_name=c_company.last_name,
        winning_amount="1000000",
        contract_number="HTLS20250606001",
        template_name="B3_"+b_company.short_name+".html"
    )
    
    print("B3-B公司邮件主题：", b_email_subject_b3)
    
    # 第一封邮件：B ➝ D（立即）
    task1 = send_reply_email.apply_async(
        args=[d_email, b_email_subject_b3, b_email_content_b3, b_smtp],
        countdown=0  # 立即
    )

    # 第二封邮件：D ➝ B（随机延迟 5–60 分钟）
    # 随机延迟 5–60 分钟
    d_email_subject_b4 = email_utils.render_email_subject(
        stage="B4",
        company_short_name=d_company.short_name,
        project_name=project_name,
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="1000000",
        winning_time="2025-06-06"
    )
    d_email_content_b4 = email_utils.render_invitation_template_content(
        buyer_name=d_company.company_name, 
        first_name=b_company.last_name_traditional,
        winning_amount="1000000",
        contract_number="HTLS20250606001",
        serial_number="L123456789",
        project_name=project_name, 
        winning_time="2025-06-06",
        template_name="B6_"+d_company.short_name+".html"
    )
    delay = random.randint(5, 60)
    task4 = send_reply_email.apply_async(
        args=[d_email, d_email_subject_b4, d_email_content_b4, d_smtp],
        countdown=delay * 60
    )

    return {
        "tasks": [
            {"step": "B ➝ D", "task_id": task1.id, "delay_min": 0},
            {"step": "D ➝ B", "task_id": task2.id, "delay_min": delay2},
        ]
    }


# BD 项目类型发送邮件
def schedule_bid_conversation_BD(b_company_name: str, d_company_name: str):
    b_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == b_company_name).first()
    d_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == d_company_name).first()

    b_smtp = {
        "host": b_company.smtp_host,
        "port": b_company.smtp_port,
        "username": b_company.smtp_username,
        "password": b_company.smtp_password,
        "from": b_company.smtp_from
    }

    d_smtp = {
        "host": d_company.smtp_host,
        "port": d_company.smtp_port,
        "username": d_company.smtp_username,
        "password": d_company.smtp_password,
        "from": d_company.smtp_from
    }

    b_email = b_company.email
    d_email = d_company.email

    # 获取对应B公司的邮件模板
    b_email_subject_b3   = render_email_subject("B3", b_company.short_name, project_name, b_company.serial_number)
    b_email_content_b3 = render_invitation_template_content(b_company_name, project_name, "b3_"+b_company.short_name+".txt")
    # 第一封邮件：B ➝ D
    task1 = send_reply_email.apply_async(
        args=[d_email, b_email_subject_b3, b_email_content_b3, b_smtp],
        countdown=0  # 立即
    )

    # 随机延迟 5–60 分钟
    d_email_subject_b4 = render_email_subject("D4", d_company.short_name, project_name, d_company.serial_number)
    d_email_content_b4 = render_invitation_template_content(d_company_name, project_name, "d4_"+d_company.short_name+".txt")
    delay2 = random.randint(5, 60)
    task2 = send_reply_email.apply_async(
        args=[b_email, d_email_subject_b4, d_email_content_b4, d_smtp],
        countdown=delay2 * 60  # 相对第一封
    )

    return {
        "tasks": [
            {"step": "B ➝ D", "task_id": task1.id, "delay_min": 0},
            {"step": "D ➝ B", "task_id": task2.id, "delay_min": delay2},
        ]
    }


# BCD 项目类型发送结算单
# 1. 发送C-B间结算单
# 2. 上一封邮件发出5-60分钟后，发送B-D间结算单
# 3. 上一封邮件发出5-60分钟后，B-D间结算单确认
# 4. 上一封邮件发出5-60分钟后，C-D间结算单确认
def schedule_settlement_BCD(
    b_company: models.CompanyInfo, 
    c_company: models.CompanyInfo, 
    d_company: models.CompanyInfo, 
    contract_serial_number: str,
    project_name: str
):

    # c_smtp = {
    #     "host": c_company.smtp_host,
    #     "port": c_company.smtp_port,
    #     "username": c_company.smtp_username,
    #     "password": c_company.smtp_password,
    #     "from": c_company.smtp_from
    # }

    b_smtp = {
        "host": "smtp.163.com",
        "port": 465,
        "username": "peterlcylove@163.com",
        "password": "ECRVsnXCe2g2Xauq",
        "from": "peterlcylove@163.com"
    }

    c_smtp = {
        "host": "smtp.qq.com",
        "port": 465,
        "username": "494762262@qq.com",
        "password": "mlnbblbyyvulbhhi",
        "from": "494762262@qq.com"
    }

    d_smtp = {
        "host": "smtp.qq.com",
        "port": 465,
        "username": "494762262@qq.com",
        "password": "mlnbblbyyvulbhhi",
        "from": "494762262@qq.com"
    }


    b_email = b_company.email
    c_email = c_company.email
    d_email = d_company.email


    # 获取对应C公司的邮件模板
    c_email_subject_c7 = email_utils.render_email_subject(
        stage="C7", 
        company_short_name=c_company.short_name, 
        project_name=project_name, 
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="100000",
        winning_time="2025-06-01"
    )
    print("c_email_subject_c7: ", c_email_subject_c7)
    c_email_content_c7 = email_utils.render_invitation_template_content(
        buyer_name="", 
        project_name=project_name, 
        serial_number="",
        first_name=b_company.last_name,
        winning_amount="100000",
        contract_number="HTLS20250606001",
        template_name="C7_"+c_company.short_name+".html"
    )
    # 第一封邮件：C ➝ B
    task1 = send_reply_email_with_attachments.apply_async(
        args=[b_email, c_email_subject_c7, c_email_content_c7, c_smtp, ["E:\\code_projects\\syjz_emails\\backend\\test_settlement.xlsx"]], # TODO 换成真实的附件路径
        countdown=0  # 立即
    )

    # 第二封邮件：B ➝ D
    # 随机延迟 5–60 分钟发出B-D间结算单
    b_email_subject_c8 = email_utils.render_email_subject(
        stage="C8", 
        company_short_name=b_company.short_name, 
        project_name=project_name, 
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="100000",
        winning_time="2025-06-01"
    )
    print("b_email_subject_c8: ", b_email_subject_c8)
    b_email_content_c8 = email_utils.render_invitation_template_content(
        buyer_name="", 
        project_name=project_name, 
        first_name=d_company.last_name,
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="100000",
        winning_time="2025-06-01",
        template_name="C8_"+b_company.short_name+".html"
    )
    # delay1 = random.randint(5, 60)
    delay1 = 1
    task2 = send_reply_email_with_attachments.apply_async(
        args=[d_email, b_email_subject_c8, b_email_content_c8, c_smtp, ["E\\code_projects\\syjz_emails\\backend\\test_settlement.xlsx"]], # TODO 换成真实的附件路径
        countdown=delay1 * 60  # 相对第一封
    )

    # 第三封邮件：D ➝ B
    # 随机延迟 5–60 分钟发出D-B间结算单确认
    d_email_subject_c9 = email_utils.render_email_subject(
        stage="C9", 
        company_short_name=d_company.short_name, 
        project_name=project_name, 
        serial_number="L123456789", 
        contract_number="HTLS20250606001", 
        winning_amount="100000", 
        winning_time="2025-06-01"
    )
    print("d_email_subject_c9: ", d_email_subject_c9)
    d_email_content_c9 = email_utils.render_invitation_template_content(
        buyer_name="", 
        project_name=project_name, 
        first_name=b_company.last_name,
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="100000",
        winning_time="2025-06-01",
        template_name="C9_"+d_company.short_name+".html"
    )
    delay2 = delay1 + 1
    task3 = send_reply_email.apply_async(
        args=[d_email, d_email_subject_c9, d_email_content_c9, d_smtp],
        countdown=delay2 * 60  # 相对第一封
    )

    # 第四封邮件：B ➝ D
    # 随机延迟 5–60 分钟发出B-D间结算单确认
    b_email_subject_c10 = email_utils.render_email_subject(
        stage="C10", 
        company_short_name=b_company.short_name, 
        project_name=project_name, 
        serial_number="L123456789", 
        contract_number="HTLS20250606001", 
        winning_amount="100000", 
        winning_time="2025-06-01"
    )
    print("b_email_subject_c10: ", b_email_subject_c10)
    b_email_content_c10 = email_utils.render_invitation_template_content(
        buyer_name="", 
        project_name=project_name, 
        first_name=c_company.last_name,
        serial_number="L123456789",
        contract_number="HTLS20250606001",
        winning_amount="100000",
        winning_time="2025-06-01",
        template_name="C10_"+b_company.short_name+".html"
    )
    delay3 = delay2 + 1
    task4 = send_reply_email.apply_async(
        args=[b_email, b_email_subject_c10, b_email_content_c10, b_smtp],
        countdown=delay3 * 60  # 相对第一封
    )

    # return {
    #     "tasks": [
    #         {"step": "C ➝ B", "task_id": task1.id, "delay_min": 0},
    #         {"step": "B ➝ C", "task_id": task2.id, "delay_min": delay1},
    #         {"step": "B ➝ D", "task_id": task3.id, "delay_min": delay2},
    #         {"step": "D ➝ B", "task_id": task4.id, "delay_min": delay3},
    #     ]
    # }

    return {"message": "任务已调度"}
    

# CCD 项目类型发送结算单
# BD之间发送结算单
def schedule_settlement_CCD(b_company_name: str, c_company_name: str, d_company_name: str):

    b_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == b_company_name).first()
    d_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == d_company_name).first()

    b_email = b_company.email
    d_email = d_company.email

    b_smtp = {
        "host": b_company.smtp_host,
        "port": b_company.smtp_port,
        "username": b_company.smtp_username,
        "password": b_company.smtp_password,
        "from": b_company.smtp_from
    }
    d_smtp = {
        "host": d_company.smtp_host,
        "port": d_company.smtp_port,
        "username": d_company.smtp_username,
        "password": d_company.smtp_password,
        "from": d_company.smtp_from
    }

    # 获取对应B公司的邮件模板
    b_email_subject_b1 = render_email_subject("B1", b_company.short_name, project_name, b_company.serial_number)
    b_email_content_b1 = render_invitation_template_content(b_company_name, project_name, "b1_"+b_company.short_name+".txt")
    # 第一封邮件：B ➝ D
    task1 = send_reply_email.apply_async(
        args=[d_email, b_email_subject_b1, b_email_content_b1, b_smtp],
        countdown=0  # 立即
    )

    # 随机延迟 5–60 分钟
    d_email_subject_d1 = render_email_subject("D1", d_company.short_name, project_name, d_company.serial_number)
    d_email_content_d1 = render_invitation_template_content(d_company_name, project_name, "d1_"+d_company.short_name+".txt")
    delay1 = random.randint(5, 60)
    task2 = send_reply_email.apply_async(
        args=[b_email, d_email_subject_d1, d_email_content_d1, d_smtp],
        countdown=delay1 * 60  # 相对第一封
    )

    return {
        "tasks": [
            {"step": "B ➝ D", "task_id": task1.id, "delay_min": 0},
            {"step": "D ➝ B", "task_id": task2.id, "delay_min": delay1},
        ]
    }

# BD 项目类型发送结算单
def schedule_settlement_BD(b_company_name: str, d_company_name: str):
    b_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == b_company_name).first()
    d_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == d_company_name).first()

    b_email = b_company.email
    d_email = d_company.email
    
    b_smtp = {
        "host": b_company.smtp_host,
        "port": b_company.smtp_port,
        "username": b_company.smtp_username,
        "password": b_company.smtp_password,
        "from": b_company.smtp_from
    }
    d_smtp = {
        "host": d_company.smtp_host,
        "port": d_company.smtp_port,
        "username": d_company.smtp_username,
        "password": d_company.smtp_password,
        "from": d_company.smtp_from
    }

    # 获取对应B公司的邮件模板
    b_email_subject_b1 = render_email_subject("B1", b_company.short_name, project_name, b_company.serial_number)
    b_email_content_b1 = render_invitation_template_content(b_company_name, project_name, "b1_"+b_company.short_name+".txt")
    
    # 第一封邮件：B ➝ D
    task1 = send_reply_email.apply_async(
        args=[d_email, b_email_subject_b1, b_email_content_b1, b_smtp],
        countdown=0  # 立即
    )
    
    # 随机延迟 5–60 分钟
    d_email_subject_d1 = render_email_subject("D1", d_company.short_name, project_name, d_company.serial_number)
    d_email_content_d1 = render_invitation_template_content(d_company_name, project_name, "d1_"+d_company.short_name+".txt")
    delay1 = random.randint(5, 60)
    task2 = send_reply_email.apply_async(
        args=[b_email, d_email_subject_d1, d_email_content_d1, d_smtp],
        countdown=delay1 * 60  # 相对第一封
    )
    
    return {
        "tasks": [
            {"step": "B ➝ D", "task_id": task1.id, "delay_min": 0},
            {"step": "D ➝ B", "task_id": task2.id, "delay_min": delay1},
        ]
    }
            

