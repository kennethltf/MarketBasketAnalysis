
SELECT 
    checkoutid,
    shopid,
    main_category,
    sub_category
    
FROM pricing_report
WHERE date_id >= DATE('2019-01-01') AND date_id <= DATE('2019-11-30')
AND shopid IN (91799978,61475131,95745694,72112289,57776355,57327530,57775788,120981896,163341072,162285147,171704932, 188348865, 43719124)
AND promo_source!='flash_sale'
