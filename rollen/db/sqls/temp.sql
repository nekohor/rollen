CREATE TABLE `temp` (
    `卷号` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `钢种` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `厚度` BIGINT(20) NULL DEFAULT NULL,
    `轧机出口平均温度` BIGINT(20) NULL DEFAULT NULL,
    `轧机出口目标温度` BIGINT(20) NULL DEFAULT NULL,
    `轧机出口温度差值` BIGINT(20) NULL DEFAULT NULL,
    `热卷卷曲平均温度` BIGINT(20) NULL DEFAULT NULL,
    `热卷卷曲目标温度` BIGINT(20) NULL DEFAULT NULL,
    `热卷卷曲温度差值` BIGINT(20) NULL DEFAULT NULL,
    `板坯平均温度` BIGINT(20) NULL DEFAULT NULL,
    `计划出炉温度` DOUBLE NULL DEFAULT NULL,
    `板坯温度差值` DOUBLE NULL DEFAULT NULL,
    `出口温度公差比` BIGINT(20) NULL DEFAULT NULL,
    `卷取温度公差比` BIGINT(20) NULL DEFAULT NULL,
    `板坯号` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `板坯出炉时间` DATETIME NULL DEFAULT NULL,
    `coil_id` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `aim_fdt` BIGINT(20) NULL DEFAULT NULL,
    `aim_ct` BIGINT(20) NULL DEFAULT NULL,
    `fdt_percent` BIGINT(20) NULL DEFAULT NULL,
    `ct_percent` BIGINT(20) NULL DEFAULT NULL,
    `datetime` DATETIME NULL DEFAULT NULL,
    `month` BIGINT(20) NULL DEFAULT NULL
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;
