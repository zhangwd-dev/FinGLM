from pypinyin import lazy_pinyin
from app.keywords import cash, balance, income


schema_meta = [
    "公司名称",
    "股票代码",
    "股票简称",
    "年份",
    "小数位数", # 用来标记金融表是几位小数
]

schema_base = [
    "外文名称", 
    "法定代表人", 
    "注册地址", 
    "办公地址", 
    "电子信箱", 
    "网址",
]

schema_emp = [
    '研发人员', 
    '技术人员', 
    "生产人员",
    "销售人员",
    "财务人员",
    "行政人员",
    '小学', 
    '初中', 
    '高中', 
    '专科', 
    '本科', 
    '硕士', 
    '博士', 
    '中专', 
    '职工总数',
]

schema_edu = [
    '小学', 
    '初中', 
    '高中',
    '中专',
    '专科', 
    '本科', 
    '硕士', 
    '博士', 
]

# 基础信息表
base = [
    "股票简称", "证券简称",
    "股票代码", "证券代码",
    "公司名称", "企业名称",
    "公司简称", "企业简称",
    "外文名称",
    "外文简称",
    "法定代表人", "法人",
    "注册地址", "注册地址的邮政编码",
    "办公地址", "办公地址的邮政编码",
    "网址", "电子信箱",
    "传真", "联系地址"
]
# 员工情况
employee = [
    '技术人员', 
    "生产人员",
    "销售人员",
    "财务人员",
    "行政人员",
    '小学', 
    '初中', 
    '高中', 
    '专科', 
    '本科', 
    '硕士', 
    '博士', 
    '中专', 
    '职工总数',
]

# 合并资产负债表
balance = [
    # '流动资产',
    '货币资金',
    '结算备付金',
    '拆出资金',
    '交易性金融资产',
    '衍生金融资产',
    '应收票据',
    '应收账款',
    '应收款项融资',
    '预付款项',
    '应收保费',
    '应收分保账款',
    '应收分保合同准备金',
    '其他应收款',
    '应收利息',
    '应收股利',
    '买入返售金融资产',
    '存货',
    '合同资产',
    '持有待售资产',
    '一年内到期的非流动资产',
    '其他流动资产',
    '流动资产合计',
    # '非流动资产',
    '发放贷款和垫款',
    '债权投资',
    '其他债权投资',
    '长期应收款',
    '长期股权投资',
    '其他权益工具投资',
    '其他非流动金融资产',
    '投资性房地产',
    '固定资产',
    '在建工程',
    '生产性生物资产',
    '油气资产',
    '使用权资产',
    '无形资产',
    '开发支出',
    '商誉',
    '长期待摊费用',
    '递延所得税资产',
    '其他非流动资产',
    '非流动资产合计',
    '资产总计',
    # '流动负债',
    '短期借款',
    '向中央银行借款',
    '拆入资金',
    '交易性金融负债',
    '衍生金融负债',
    '应付票据',
    '应付账款',
    '预收款项',
    '合同负债',
    '卖出回购金融资产款',
    '吸收存款及同业存放',
    '代理买卖证券款',
    '代理承销证券款',
    '应付职工薪酬',
    '应交税费',
    '其他应付款',
    '应付利息',
    '应付股利',
    '应付手续费及佣金',
    '应付分保账款',
    '持有待售负债',
    '一年内到期的非流动负债',
    '其他流动负债',
    '流动负债合计',
    # '非流动负债',
    '保险合同准备金',
    '长期借款',
    '应付债券',
    '租赁负债',
    '长期应付款',
    '长期应付职工薪酬',
    '预计负债',
    '递延收益',
    '递延所得税负债',
    '其他非流动负债',
    '非流动负债合计',
    '负债合计',
    # '所有者权益',
    '股本',
    '其他权益工具',
    '优先股',
    '永续债',
    '资本公积',
    '库存股',
    '其他综合收益',
    '专项储备',
    '盈余公积',
    '一般风险准备',
    '未分配利润',
    '归属于母公司所有者权益合计',
    '少数股东权益',
    '所有者权益合计',
    '负债和所有者权益总计'
]

# 现金流量表
cash = [
    # '经营活动产生的现金流量',
    '销售商品、提供劳务收到的现金',
    '客户存款和同业存放款项净增加额',
    '向中央银行借款净增加额',
    '向其他金融机构拆入资金净增加额',
    '收到原保险合同保费取得的现金',
    '收到再保业务现金净额',
    '保户储金及投资款净增加额',
    '收取利息、手续费及佣金的现金',
    '拆入资金净增加额',
    '回购业务资金净增加额',
    '代理买卖证券收到的现金净额',
    '收到的税费返还',
    '收到其他与经营活动有关的现金',
    '经营活动现金流入小计',
    '购买商品、接受劳务支付的现金',
    '客户贷款及垫款净增加额',
    '存放中央银行和同业款项净增加额',
    '支付原保险合同赔付款项的现金',
    '拆出资金净增加额',
    '支付利息、手续费及佣金的现金',
    '支付保单红利的现金',
    '支付给职工以及为职工支付的现金',
    '支付的各项税费',
    '支付其他与经营活动有关的现金',
    '经营活动现金流出小计',
    '经营活动产生的现金流量净额',
    # '投资活动产生的现金流量',
    '收回投资收到的现金',
    '取得投资收益收到的现金',
    '处置固定资产、无形资产和其他长期资产收回',
    '处置子公司及其他营业单位收到的现金净额',
    '收到其他与投资活动有关的现金',
    '投资活动现金流入小计',
    '购建固定资产、无形资产和其他长期资产支付',
    '投资支付的现金',
    '质押贷款净增加额',
    '取得子公司及其他营业单位支付的现金净额',
    '支付其他与投资活动有关的现金',
    '投资活动现金流出小计',
    '投资活动产生的现金流量净额',
    # '筹资活动产生的现金流量',
    '吸收投资收到的现金',
    '子公司吸收少数股东投资收到的现金',
    '取得借款收到的现金',
    '收到其他与筹资活动有关的现金',
    '筹资活动现金流入小计',
    '偿还债务支付的现金',
    '分配股利、利润或偿付利息支付的现金',
    '子公司支付给少数股东的股利、利润',
    '支付其他与筹资活动有关的现金',
    '筹资活动现金流出小计',
    '筹资活动产生的现金流量净额',
    '汇率变动对现金及现金等价物的影响',
    '现金及现金等价物净增加额',
    '期初现金及现金等价物余额',
    '期末现金及现金等价物余额'
]

# 合并利润表
income = [
    '营业总收入',
    '营业收入',
    '已赚保费',
    '手续费及佣金收入',
    '营业总成本',
    '营业成本',
    '利息支出',
    '手续费及佣金支出',
    '退保金',
    '赔付支出净额',
    '提取保险责任合同准备金净额',
    '保单红利支出',
    '分保费用',
    '税金及附加',
    '销售费用',
    '管理费用',
    '研发费用',
    '财务费用',
    '利息费用',
    '利息收入',
    '其他收益',
    '投资收益',
    '对联营企业和合营企业的投资收益',
    '以摊余成本计量的金融资产终止确认收益',
    '汇兑收益',
    '净敞口套期收益',
    '公允价值变动收益',
    '信用减值损失',
    '资产减值损失',
    '资产处置收益',
    '营业利润',
    '营业外收入',
    '营业外支出',
    '利润总额',
    '所得税费用',
    '净利润',
    '持续经营净利润',
    '终止经营净利润',
    '归属于母公司股东的净利润',
    '少数股东损益',
    '其他综合收益的税后净额',
    '归属母公司所有者的其他综合收益的税后净额',
    '不能重分类进损益的其他综合收益',
    '重新计量设定受益计划变动额',
    '权益法下不能转损益的其他综合收益',
    '其他权益工具投资公允价值变动',
    '企业自身信用风险公允价值变动',
    '将重分类进损益的其他综合收益',
    '权益法下可转损益的其他综合收益',
    '其他债权投资公允价值变动',
    '金融资产重分类计入其他综合收益的金额',
    '其他债权投资信用减值准备',
    '现金流量套期储备',
    '外币财务报表折算差额',
    '归属于少数股东的其他综合收益的税后净额',
    '综合收益总额',
    '归属于母公司所有者的综合收益总额',
    '归属于少数股东的综合收益总额',
    '基本每股收益',
    '稀释每股收益'
]

schema_fin = balance + cash + income

schema = schema_meta + schema_base + schema_fin +schema_emp

schema_py2zh = {"_".join(lazy_pinyin(i)): i for i in schema}

schema_zh2py = {v: k for k, v in schema_py2zh.items()}

# DDL
# CREATE TABLE three_big_tables (
#         gong_si_ming_cheng TEXT,
# gu_piao_dai_ma TEXT,
# gu_piao_jian_cheng TEXT,
# nian_fen TEXT,
# liu_dong_zi_chan TEXT,
# huo_bi_zi_jin TEXT,
# jie_suan_bei_fu_jin TEXT,
# chai_chu_zi_jin TEXT,
# jiao_yi_xing_jin_rong_zi_chan TEXT,
# yi_gong_yun_jia_zhi_ji_liang_qie_qi_bian_dong_ji_ru_dang_qi_sun_yi_de_jin_rong_zi_chan TEXT,
# yan_sheng_jin_rong_zi_chan TEXT,
# ying_shou_piao_ju TEXT,
# ying_shou_zhang_kuan TEXT,
# ying_shou_kuan_xiang_rong_zi TEXT,
# yu_fu_kuan_xiang TEXT,
# ying_shou_bao_fei TEXT,
# ying_shou_fen_bao_zhang_kuan TEXT,
# ying_shou_fen_bao_he_tong_zhun_bei_jin TEXT,
# qi_ta_ying_shou_kuan TEXT,
# ying_shou_li_xi TEXT,
# ying_shou_gu_li TEXT,
# mai_ru_fan_shou_jin_rong_zi_chan TEXT,
# cun_huo TEXT,
# he_tong_zi_chan TEXT,
# chi_you_dai_shou_zi_chan TEXT,
# yi_nian_nei_dao_qi_de_fei_liu_dong_zi_chan TEXT,
# qi_ta_liu_dong_zi_chan TEXT,
# liu_dong_zi_chan_he_ji TEXT,
# fei_liu_dong_zi_chan TEXT,
# fa_fang_dai_kuan_he_dian_kuan TEXT,
# zhai_quan_tou_zi TEXT,
# ke_gong_chu_shou_jin_rong_zi_chan TEXT,
# qi_ta_zhai_quan_tou_zi TEXT,
# chi_you_zhi_dao_qi_tou_zi TEXT,
# chang_qi_ying_shou_kuan TEXT,
# chang_qi_gu_quan_tou_zi TEXT,
# qi_ta_quan_yi_gong_ju_tou_zi TEXT,
# qi_ta_fei_liu_dong_jin_rong_zi_chan TEXT,
# tou_zi_xing_fang_di_chan TEXT,
# gu_ding_zi_chan TEXT,
# zai_jian_gong_cheng TEXT,
# sheng_chan_xing_sheng_wu_zi_chan TEXT,
# you_qi_zi_chan TEXT,
# shi_yong_quan_zi_chan TEXT,
# wu_xing_zi_chan TEXT,
# kai_fa_zhi_chu TEXT,
# shang_yu TEXT,
# chang_qi_dai_tan_fei_yong TEXT,
# di_yan_suo_de_shui_zi_chan TEXT,
# qi_ta_fei_liu_dong_zi_chan TEXT,
# fei_liu_dong_zi_chan_he_ji TEXT,
# zi_chan_zong_ji TEXT,
# liu_dong_fu_zhai TEXT,
# duan_qi_jie_kuan TEXT,
# xiang_zhong_yang_yin_hang_jie_kuan TEXT,
# chai_ru_zi_jin TEXT,
# jiao_yi_xing_jin_rong_fu_zhai TEXT,
# yi_gong_yun_jia_zhi_ji_liang_qie_qi_bian_dong_ji_ru_dang_qi_sun_yi_de_jin_rong_fu_zhai TEXT,
# yan_sheng_jin_rong_fu_zhai TEXT,
# ying_fu_piao_ju TEXT,
# ying_fu_zhang_kuan TEXT,
# yu_shou_kuan_xiang TEXT,
# he_tong_fu_zhai TEXT,
# mai_chu_hui_gou_jin_rong_zi_chan_kuan TEXT,
# xi_shou_cun_kuan_ji_tong_ye_cun_fang TEXT,
# dai_li_mai_mai_zheng_quan_kuan TEXT,
# dai_li_cheng_xiao_zheng_quan_kuan TEXT,
# ying_fu_zhi_gong_xin_chou TEXT,
# ying_jiao_shui_fei TEXT,
# qi_ta_ying_fu_kuan TEXT,
# ying_fu_li_xi TEXT,
# ying_fu_gu_li TEXT,
# ying_fu_shou_xu_fei_ji_yong_jin TEXT,
# ying_fu_fen_bao_zhang_kuan TEXT,
# chi_you_dai_shou_fu_zhai TEXT,
# yi_nian_nei_dao_qi_de_fei_liu_dong_fu_zhai TEXT,
# qi_ta_liu_dong_fu_zhai TEXT,
# liu_dong_fu_zhai_he_ji TEXT,
# fei_liu_dong_fu_zhai TEXT,
# bao_xian_he_tong_zhun_bei_jin TEXT,
# chang_qi_jie_kuan TEXT,
# ying_fu_zhai_quan TEXT,
# you_xian_gu TEXT,
# yong_xu_zhai TEXT,
# zu_lin_fu_zhai TEXT,
# chang_qi_ying_fu_kuan TEXT,
# chang_qi_ying_fu_zhi_gong_xin_chou TEXT,
# yu_ji_fu_zhai TEXT,
# di_yan_shou_yi TEXT,
# di_yan_suo_de_shui_fu_zhai TEXT,
# qi_ta_fei_liu_dong_fu_zhai TEXT,
# fei_liu_dong_fu_zhai_he_ji TEXT,
# fu_zhai_he_ji TEXT,
# suo_you_zhe_quan_yi TEXT,
# gu_ben TEXT,
# qi_ta_quan_yi_gong_ju TEXT,
# zi_ben_gong_ji TEXT,
# ku_cun_gu TEXT,
# qi_ta_zong_he_shou_yi TEXT,
# zhuan_xiang_chu_bei TEXT,
# ying_yu_gong_ji TEXT,
# yi_ban_feng_xian_zhun_bei TEXT,
# wei_fen_pei_li_run TEXT,
# gui_shu_yu_mu_gong_si_suo_you_zhe_quan_yi_he_ji TEXT,
# shao_shu_gu_dong_quan_yi TEXT,
# suo_you_zhe_quan_yi_he_ji TEXT,
# fu_zhai_he_suo_you_zhe_quan_yi_zong_ji TEXT,
# ying_ye_zong_shou_ru TEXT,
# ying_ye_shou_ru TEXT,
# li_xi_shou_ru TEXT,
# yi_zhuan_bao_fei TEXT,
# shou_xu_fei_ji_yong_jin_shou_ru TEXT,
# ying_ye_zong_cheng_ben TEXT,
# ying_ye_cheng_ben TEXT,
# li_xi_zhi_chu TEXT,
# shou_xu_fei_ji_yong_jin_zhi_chu TEXT,
# tui_bao_jin TEXT,
# pei_fu_zhi_chu_jing_e TEXT,
# ti_qu_bao_xian_ze_ren_he_tong_zhun_bei_jin_jing_e TEXT,
# bao_dan_hong_li_zhi_chu TEXT,
# fen_bao_fei_yong TEXT,
# shui_jin_ji_fu_jia TEXT,
# xiao_shou_fei_yong TEXT,
# guan_li_fei_yong TEXT,
# yan_fa_fei_yong TEXT,
# cai_wu_fei_yong TEXT,
# li_xi_fei_yong TEXT,
# qi_ta_shou_yi TEXT,
# tou_zi_shou_yi TEXT,
# dui_lian_ying_qi_ye_he_he_ying_qi_ye_de_tou_zi_shou_yi TEXT,
# yi_tan_yu_cheng_ben_ji_liang_de_jin_rong_zi_chan_zhong_zhi_que_ren_shou_yi TEXT,
# hui_dui_shou_yi TEXT,
# jing_chang_kou_tao_qi_shou_yi TEXT,
# gong_yun_jia_zhi_bian_dong_shou_yi TEXT,
# xin_yong_jian_zhi_sun_shi TEXT,
# zi_chan_jian_zhi_sun_shi TEXT,
# zi_chan_chu_zhi_shou_yi TEXT,
# ying_ye_li_run TEXT,
# ying_ye_wai_shou_ru TEXT,
# ying_ye_wai_zhi_chu TEXT,
# li_run_zong_e TEXT,
# suo_de_shui_fei_yong TEXT,
# jing_li_run TEXT,
# an_jing_ying_chi_xu_xing_fen_lei TEXT,
# chi_xu_jing_ying_jing_li_run TEXT,
# zhong_zhi_jing_ying_jing_li_run TEXT,
# an_suo_you_quan_gui_shu_fen_lei TEXT,
# gui_shu_yu_mu_gong_si_suo_you_zhe_de_jing_li_run TEXT,
# shao_shu_gu_dong_sun_yi TEXT,
# qi_ta_zong_he_shou_yi_de_shui_hou_jing_e TEXT,
# gui_shu_mu_gong_si_suo_you_zhe_de_qi_ta_zong_he_shou_yi_de_shui_hou_jing_e TEXT,
# bu_neng_zhong_fen_lei_jin_sun_yi_de_qi_ta_zong_he_shou_yi TEXT,
# chong_xin_ji_liang_she_ding_shou_yi_ji_hua_bian_dong_e TEXT,
# quan_yi_fa_xia_bu_neng_zhuan_sun_yi_de_qi_ta_zong_he_shou_yi TEXT,
# qi_ta_quan_yi_gong_ju_tou_zi_gong_yun_jia_zhi_bian_dong TEXT,
# qi_ye_zi_shen_xin_yong_feng_xian_gong_yun_jia_zhi_bian_dong TEXT,
# jiang_zhong_fen_lei_jin_sun_yi_de_qi_ta_zong_he_shou_yi TEXT,
# quan_yi_fa_xia_ke_zhuan_sun_yi_de_qi_ta_zong_he_shou_yi TEXT,
# qi_ta_zhai_quan_tou_zi_gong_yun_jia_zhi_bian_dong TEXT,
# ke_gong_chu_shou_jin_rong_zi_chan_gong_yun_jia_zhi_bian_dong_sun_yi TEXT,
# jin_rong_zi_chan_zhong_fen_lei_ji_ru_qi_ta_zong_he_shou_yi_de_jin_e TEXT,
# chi_you_zhi_dao_qi_tou_zi_zhong_fen_lei_wei_ke_gong_chu_shou_jin_rong_zi_chan_sun_yi TEXT,
# qi_ta_zhai_quan_tou_zi_xin_yong_jian_zhi_zhun_bei TEXT,
# xian_jin_liu_liang_tao_qi_chu_bei TEXT,
# wai_bi_cai_wu_bao_biao_zhe_suan_cha_e TEXT,
# gui_shu_yu_shao_shu_gu_dong_de_qi_ta_zong_he_shou_yi_de_shui_hou_jing_e TEXT,
# zong_he_shou_yi_zong_e TEXT,
# gui_shu_yu_mu_gong_si_suo_you_zhe_de_zong_he_shou_yi_zong_e TEXT,
# gui_shu_yu_shao_shu_gu_dong_de_zong_he_shou_yi_zong_e TEXT,
# mei_gu_shou_yi TEXT,
# ji_ben_mei_gu_shou_yi TEXT,
# xi_shi_mei_gu_shou_yi TEXT,
# jing_ying_huo_dong_chan_sheng_de_xian_jin_liu_liang TEXT,
# xiao_shou_shang_pin_、_ti_gong_lao_wu_shou_dao_de_xian_jin TEXT,
# ke_hu_cun_kuan_he_tong_ye_cun_fang_kuan_xiang_jing_zeng_jia_e TEXT,
# xiang_zhong_yang_yin_hang_jie_kuan_jing_zeng_jia_e TEXT,
# xiang_qi_ta_jin_rong_ji_gou_chai_ru_zi_jin_jing_zeng_jia_e TEXT,
# shou_dao_yuan_bao_xian_he_tong_bao_fei_qu_de_de_xian_jin TEXT,
# shou_dao_zai_bao_ye_wu_xian_jin_jing_e TEXT,
# bao_hu_chu_jin_ji_tou_zi_kuan_jing_zeng_jia_e TEXT,
# shou_qu_li_xi_、_shou_xu_fei_ji_yong_jin_de_xian_jin TEXT,
# chai_ru_zi_jin_jing_zeng_jia_e TEXT,
# hui_gou_ye_wu_zi_jin_jing_zeng_jia_e TEXT,
# dai_li_mai_mai_zheng_quan_shou_dao_de_xian_jin_jing_e TEXT,
# shou_dao_de_shui_fei_fan_huan TEXT,
# shou_dao_qi_ta_yu_jing_ying_huo_dong_you_guan_de_xian_jin TEXT,
# jing_ying_huo_dong_xian_jin_liu_ru_xiao_ji TEXT,
# gou_mai_shang_pin_、_jie_shou_lao_wu_zhi_fu_de_xian_jin TEXT,
# ke_hu_dai_kuan_ji_dian_kuan_jing_zeng_jia_e TEXT,
# cun_fang_zhong_yang_yin_hang_he_tong_ye_kuan_xiang_jing_zeng_jia_e TEXT,
# zhi_fu_yuan_bao_xian_he_tong_pei_fu_kuan_xiang_de_xian_jin TEXT,
# chai_chu_zi_jin_jing_zeng_jia_e TEXT,
# zhi_fu_li_xi_、_shou_xu_fei_ji_yong_jin_de_xian_jin TEXT,
# zhi_fu_bao_dan_hong_li_de_xian_jin TEXT,
# zhi_fu_gei_zhi_gong_yi_ji_wei_zhi_gong_zhi_fu_de_xian_jin TEXT,
# zhi_fu_de_ge_xiang_shui_fei TEXT,
# zhi_fu_qi_ta_yu_jing_ying_huo_dong_you_guan_de_xian_jin TEXT,
# jing_ying_huo_dong_xian_jin_liu_chu_xiao_ji TEXT,
# jing_ying_huo_dong_chan_sheng_de_xian_jin_liu_liang_jing_e TEXT,
# tou_zi_huo_dong_chan_sheng_de_xian_jin_liu_liang TEXT,
# shou_hui_tou_zi_shou_dao_de_xian_jin TEXT,
# qu_de_tou_zi_shou_yi_shou_dao_de_xian_jin TEXT,
# chu_zhi_gu_ding_zi_chan_、_wu_xing_zi_chan_he_qi_ta_chang_qi_zi_chan_shou_hui_de_xian_jin_jing_e TEXT,
# chu_zhi_zi_gong_si_ji_qi_ta_ying_ye_dan_wei_shou_dao_de_xian_jin_jing_e TEXT,
# shou_dao_qi_ta_yu_tou_zi_huo_dong_you_guan_de_xian_jin TEXT,
# tou_zi_huo_dong_xian_jin_liu_ru_xiao_ji TEXT,
# gou_jian_gu_ding_zi_chan_、_wu_xing_zi_chan_he_qi_ta_chang_qi_zi_chan_zhi_fu_de_xian_jin TEXT,
# tou_zi_zhi_fu_de_xian_jin TEXT,
# zhi_ya_dai_kuan_jing_zeng_jia_e TEXT,
# qu_de_zi_gong_si_ji_qi_ta_ying_ye_dan_wei_zhi_fu_de_xian_jin_jing_e TEXT,
# zhi_fu_qi_ta_yu_tou_zi_huo_dong_you_guan_de_xian_jin TEXT,
# tou_zi_huo_dong_xian_jin_liu_chu_xiao_ji TEXT,
# tou_zi_huo_dong_chan_sheng_de_xian_jin_liu_liang_jing_e TEXT,
# chou_zi_huo_dong_chan_sheng_de_xian_jin_liu_liang TEXT,
# xi_shou_tou_zi_shou_dao_de_xian_jin TEXT,
# zi_gong_si_xi_shou_shao_shu_gu_dong_tou_zi_shou_dao_de_xian_jin TEXT,
# qu_de_jie_kuan_shou_dao_de_xian_jin TEXT,
# shou_dao_qi_ta_yu_chou_zi_huo_dong_you_guan_de_xian_jin TEXT,
# chou_zi_huo_dong_xian_jin_liu_ru_xiao_ji TEXT,
# chang_huan_zhai_wu_zhi_fu_de_xian_jin TEXT,
# fen_pei_gu_li_、_li_run_huo_chang_fu_li_xi_zhi_fu_de_xian_jin TEXT,
# zi_gong_si_zhi_fu_gei_shao_shu_gu_dong_de_gu_li_、_li_run TEXT,
# zhi_fu_qi_ta_yu_chou_zi_huo_dong_you_guan_de_xian_jin TEXT,
# chou_zi_huo_dong_xian_jin_liu_chu_xiao_ji TEXT,
# chou_zi_huo_dong_chan_sheng_de_xian_jin_liu_liang_jing_e TEXT,
# hui_lv_bian_dong_dui_xian_jin_ji_xian_jin_deng_jia_wu_de_ying_xiang TEXT,
# xian_jin_ji_xian_jin_deng_jia_wu_jing_zeng_jia_e TEXT,
# qi_chu_xian_jin_ji_xian_jin_deng_jia_wu_yu_e TEXT,
# qi_mo_xian_jin_ji_xian_jin_deng_jia_wu_yu_e TEXT
#     );
if __name__ == "__main__":
    print(len(schema))