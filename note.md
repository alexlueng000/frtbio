494762262@qq.com mlnbblbyyvulbhhi
接收邮件服务器： pop.qq.com，使用SSL，端口号995
发送邮件服务器： smtp.qq.com，使用SSL，端口号465或587


测试数据：

B公司：深圳市深业晋展物料供应有限公司
C公司：深圳市立达方圆物料供应有限公司
D公司：PRECISE INSTRUMENT COMPANY LIMITED

项目名称：testproject1
合同编号：HTLS20250606001
中标金额：1000000
中标时间：2025-06-06
流水号：L123456789


INSERT INTO email_subject (stage, company_name, short_name, subject)
VALUES
    ('A2', '深圳市深业晋展物料供应有限公司', 'JZ', '{project_name} {serial_number}'),
    ('A2', '深圳市弗劳恩科技服务有限公司', 'FW', '{project_name} 编号：{serial_number}'), 
    ('A2', '深圳市立达方圆物料供应有限公司', 'LD', '{project_name} {serial_number}'),
    ('A2', '深圳市德贯科技有限公司', 'DG', '{project_name} {serial_number}'),
    ('A2', '深圳市赛纳精密仪器有限公司', 'SN', '{project_name} 投标委托确认 {serial_number}'),
    ('A2', '深圳市拓踏科技有限公司', 'TT', '{project_name}_投标回复_{serial_number}'),
    ('A2', '深圳市智翰仪器有限公司', 'ZH', '{project_name} {serial_number}'),
    ('A2', '深圳市乔孚科技有限公司', 'QF', '{project_name} {serial_number}'),
    ('A2', '深圳市泽意仪器有限公司', 'ZY', '【投标委托确认】{project_name} {serial_number}'),
    ('A2', '深圳市久业科技仪器有限公司', 'JY', '【回复确认】{project_name} {serial_number}'),
    ('A2', '深圳市雅怡科技仪器有限公司', 'YY', '{project_name}/{serial_number}'),
    ('A2', '深圳市启慧仪器有限公司', 'QH', '{project_name} {serial_number}'),
    ('A2', '深圳市佰志诚科技发展有限公司', 'BZC', '{project_name} {serial_number}'),
    ('A2', '深圳市礼恒科技有限公司', 'LH', '{project_name} {serial_number}'),
    ('A2', '深圳市海辰星科技有限公司', 'HCX', '{project_name} 投标委托确认 {serial_number}');


project_fee_details:
id,
project_id (foreign key),
中标时间
中标金额,
三方/四方货款，
进口服务费，
第三方费用，
费用结算服务费，
中标服务费，
购买标书费，
投标服务费，


CREATE TABLE project_fee_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    winning_time DATE,                        -- 中标时间
    winning_amount DECIMAL(15,2),             -- 中标金额
    three_fourth_amount DECIMAL(15,2),        -- 三方/四方货款
    import_service_fee DECIMAL(15,2),         -- 进口服务费
    third_party_fee DECIMAL(15,2),            -- 第三方费用
    settlement_service_fee DECIMAL(15,2),     -- 费用结算服务费
    bidding_service_fee DECIMAL(15,2),        -- 中标服务费
    document_purchase_fee DECIMAL(15,2),      -- 购买标书费
    tender_service_fee DECIMAL(15,2),         -- 投标服务费
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (project_id) REFERENCES project_info(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




"body": "{\"contract_type\":\"1\",\"f_serial_number\":\"1\",\"company_b_name\":\"1\",\"contract_number\":\"1\",\"company_c_name\":\"1\",\"winning_time\":\"1\",\"contract_serial_number\":\"1\",\"company_d_name\":\"1\",\"project_name\":[{\"numberField_l7ps2caa\":\"954687321\",\"radioField_lfafvypp\":\"否\",\"selectField_la4orihe\":\"ANTON PAAR GMBH\",\"selectField_l7ps2ca3\":\"三方/四方合同\",\"numberField_leqpuqk4\":\"\",\"selectField_l7ps2ca8\":\"CNY\",\"numberField_l7ps2ca9\":\"1\",\"selectField_l7ps2ca7\":\"FRAUN SCIENCE AND TECHNOLOGY SERVICE COMPANY LIMITED\",\"selectField_l7ps2ca6\":\"深圳市立达方圆物料供应有限公司\",\"numberField_lfafvypq\":\"\",\"selectField_l7ps2ca5\":\"付\"}],\"l_serial_number\":\"1\",\"winning_amount\":\"1\",\"p_serial_number\":\"1\"}",