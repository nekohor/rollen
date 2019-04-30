CREATE TABLE `cid` (
    `coil_id` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `start_date` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `datetime` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `steel_grade` TEXT NULL COLLATE 'utf8mb4_unicode_ci',
    `coil_len` DOUBLE NULL DEFAULT NULL,
    `aim_thick` DOUBLE NULL DEFAULT NULL,
    `aim_width` DOUBLE NULL DEFAULT NULL,
    `aim_crown` DOUBLE NULL DEFAULT NULL,
    `aim_fdt` DOUBLE NULL DEFAULT NULL,
    `aim_ct` DOUBLE NULL DEFAULT NULL,
    `month` BIGINT(20) NULL DEFAULT NULL
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;
