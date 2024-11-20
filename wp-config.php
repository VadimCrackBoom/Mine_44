<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wp_SITE-45' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'root' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'zct<R[ETS!XA;LY= @P+|gd0lvNVHA;C O`^lbOi3+rd(f6ey6+f~*c)pWs]kS~7' );
define( 'SECURE_AUTH_KEY',  'pSNol.U7,]=x.)9/lAU}t,NLIQ+egr?*>?;Thv(r%VysTxA+,AIvs+@lnqdhR {B' );
define( 'LOGGED_IN_KEY',    'CXOnP Y(B;p50*GqT XlOw1-J}?Mfrh^=>/v_sd0+Y&JQc_w^&3]`6g6v/T.}#YS' );
define( 'NONCE_KEY',        'a*B{jN2fb)C ,mVT5J9=E4PjtrsTD.d6}Z9FBasdN!=/=+;f|+jQpY~$}4Sl5@0E' );
define( 'AUTH_SALT',        'V=+IK[i;|#aSS&S,Y7eJu|>0ipX.};#ezBan,m ,zube/D66O*`_aTVA)([rw1pt' );
define( 'SECURE_AUTH_SALT', '?9*A`a*mnBRy<$6KnB^NWL0{p.X~R48mhcq}qzeuDR)!(x+pUJrh;S07hXd5sUu&' );
define( 'LOGGED_IN_SALT',   'kFXu8s*;8nfC$W~PfY43%YkhP+Ui!1&O{k2]YQ{eDQ8J|G~-zk#QSjR<_j!{ ^xP' );
define( 'NONCE_SALT',       'F*7Beo)Iioa]^j<7c.[df+Xo={E<~%GpyM(Kq`^3VdtK&.`B|_jH$b/y+gP5IM?>' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
