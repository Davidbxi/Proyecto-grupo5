-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 13-10-2023 a las 03:41:13
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_comite`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comite`
--

CREATE TABLE `comite` (
  `id_comite` int(20) NOT NULL,
  `nom_comite` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comite`
--

INSERT INTO `comite` (`id_comite`, `nom_comite`) VALUES
(1, 'Bajo rendiemiento'),
(2, 'Mal rendimiento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL,
  `nom_estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ficha`
--

CREATE TABLE `ficha` (
  `id_comite` int(11) NOT NULL,
  `num_ficha` varchar(20) NOT NULL,
  `nom_ficha` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_solicitud`
--

CREATE TABLE `tbl_solicitud` (
  `num_doc` int(20) NOT NULL,
  `tipo_doc` varchar(30) NOT NULL,
  `p_nombre` varchar(50) NOT NULL,
  `s_nombre` varchar(20) DEFAULT NULL,
  `p_apellido` varchar(50) NOT NULL,
  `s_apellido` varchar(20) DEFAULT NULL,
  `id_ficha` varchar(11) NOT NULL,
  `id_comite` varchar(50) NOT NULL,
  `fecha_asig` varchar(50) NOT NULL,
  `observacion` varchar(100) DEFAULT NULL,
  `id_estado` varchar(30) NOT NULL,
  `fecha_registro` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tbl_solicitud`
--

INSERT INTO `tbl_solicitud` (`num_doc`, `tipo_doc`, `p_nombre`, `s_nombre`, `p_apellido`, `s_apellido`, `id_ficha`, `id_comite`, `fecha_asig`, `observacion`, `id_estado`, `fecha_registro`) VALUES
(1125484, '2', 'Aura', 'Cristina', 'romero', '', '2', '1', '2023-10-23', 'ninguno', '2', '2023-10-12 16:22:18'),
(10218484, '1', 'David', '', 'Bedoya', '', '2', '1', '2023-10-12', 'ninguno', '2', '2023-10-12 05:54:31'),
(12156648, '1', 'luz', 'del carmen', 'padilla', 'mendoza', '1', '1', '2023-10-12', 'Ninguna', '3', '2023-10-12 18:53:00'),
(1028018279, '1', 'Oscar', 'miguel', 'romero', 'yanez', '1', '1', '2023-10-11', 'oscar', '2', '2023-10-12 03:26:28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name_surname` varchar(100) NOT NULL,
  `email_user` varchar(50) NOT NULL,
  `pass_user` text NOT NULL,
  `created_user` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name_surname`, `email_user`, `pass_user`, `created_user`) VALUES
(4, 'oscar romero', 'oscar@gmail.com', 'scrypt:32768:8:1$C31K7nw9vgbN2Mzo$25c92a57cbd83739a84569c74246524dfb35e58a79c3e0d6a518b18cad2c5c981e1c3898603cfc1646f92d6dc4cb9e9d4b9fba3ade986ddffdb98bcb29f5b72e', '2023-10-12 16:55:06'),
(5, 'David Bedoya', 'david@gmail.com', 'scrypt:32768:8:1$T7Dawlw6Bi7NoBWC$946d98cf0f7134a3a14a77e6a88e2a6525de6b8e83fe8d0e918d7272ccfa62649b0721941beed4ebcf3ea4c3dd36f74411562e7d08fdf9564f96a77cc74f93ea', '2023-10-12 19:19:27');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comite`
--
ALTER TABLE `comite`
  ADD PRIMARY KEY (`id_comite`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `ficha`
--
ALTER TABLE `ficha`
  ADD PRIMARY KEY (`id_comite`);

--
-- Indices de la tabla `tbl_solicitud`
--
ALTER TABLE `tbl_solicitud`
  ADD PRIMARY KEY (`num_doc`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comite`
--
ALTER TABLE `comite`
  MODIFY `id_comite` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `estado`
--
ALTER TABLE `estado`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ficha`
--
ALTER TABLE `ficha`
  MODIFY `id_comite` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
