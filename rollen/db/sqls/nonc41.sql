CREATE TABLE `nonc41` (
    `卷号` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `生产时间` BIGINT(20) NULL DEFAULT NULL,
    `平直度平均值` DOUBLE NULL DEFAULT NULL,
    `平直度最大值` DOUBLE NULL DEFAULT NULL,
    `平直度最小值` DOUBLE NULL DEFAULT NULL,
    `钢种` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `平均宽度` BIGINT(20) NULL DEFAULT NULL,
    `平均厚度` DOUBLE NULL DEFAULT NULL,
    `浪形` BIGINT(20) NULL DEFAULT NULL,
    `coil_id` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `datetime` BIGINT(20) NULL DEFAULT NULL,
    `month` BIGINT(20) NULL DEFAULT NULL
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;
