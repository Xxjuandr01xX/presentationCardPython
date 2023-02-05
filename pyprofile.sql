-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-02-2023 a las 22:04:23
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pyprofile`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `py_experiencia_laboral`
--

CREATE TABLE `py_experiencia_laboral` (
  `id` int(11) NOT NULL,
  `nom_empresa` varchar(100) NOT NULL,
  `fech_ingreso` date NOT NULL,
  `fech_fin` date NOT NULL,
  `ocupacion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `py_pais`
--

CREATE TABLE `py_pais` (
  `id` int(11) NOT NULL,
  `cod_tel` varchar(4) NOT NULL,
  `denominacion` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `py_pais`
--

INSERT INTO `py_pais` (`id`, `cod_tel`, `denominacion`) VALUES
(1, '+058', 'VENEZUELA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `py_profile_person`
--

CREATE TABLE `py_profile_person` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `profesion` varchar(20) NOT NULL,
  `direccion` text NOT NULL,
  `fec_nac` date NOT NULL,
  `id_pais_fk` int(11) NOT NULL,
  `id_elab_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `py_profile_person`
--

INSERT INTO `py_profile_person` (`id`, `nombre`, `apellido`, `correo`, `telefono`, `profesion`, `direccion`, `fec_nac`, `id_pais_fk`, `id_elab_fk`) VALUES
(1, 'JUAN DIEGO', 'RINCON URDANETA', 'jd.rincon021@gmail.com', '(414)-6801859', 'INGENIERO DE SISTEMA', 'Calle 79E #79-40, Sector macandona 2 Av la Limpia.', '1994-12-13', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `py_rol`
--

CREATE TABLE `py_rol` (
  `id` int(11) NOT NULL,
  `denominacion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `py_rol`
--

INSERT INTO `py_rol` (`id`, `denominacion`) VALUES
(1, 'ADMINISTRADOR'),
(2, 'NORMAL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `py_slides`
--

CREATE TABLE `py_slides` (
  `id` int(11) NOT NULL,
  `title` varchar(30) NOT NULL,
  `dir_image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `py_slides`
--

INSERT INTO `py_slides` (`id`, `title`, `dir_image`) VALUES
(2, 'slider N01', 'static/img/slides/Soluciones_IT_-_RZ.png'),
(3, 'slider N02', 'static/img/slides/jUAN_D._RINCON_U._-_RZ.png'),
(4, 'slider N03', 'static/img/slides/Development_application.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `py_userse`
--

CREATE TABLE `py_userse` (
  `id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `passwd` varchar(100) NOT NULL,
  `id_rol_fk` int(11) NOT NULL,
  `id_persona_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `py_userse`
--

INSERT INTO `py_userse` (`id`, `username`, `passwd`, `id_rol_fk`, `id_persona_fk`) VALUES
(1, 'admin', '*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9', 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `py_experiencia_laboral`
--
ALTER TABLE `py_experiencia_laboral`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `py_pais`
--
ALTER TABLE `py_pais`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `py_profile_person`
--
ALTER TABLE `py_profile_person`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `py_rol`
--
ALTER TABLE `py_rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `py_slides`
--
ALTER TABLE `py_slides`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `py_userse`
--
ALTER TABLE `py_userse`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `py_experiencia_laboral`
--
ALTER TABLE `py_experiencia_laboral`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `py_pais`
--
ALTER TABLE `py_pais`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `py_profile_person`
--
ALTER TABLE `py_profile_person`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `py_rol`
--
ALTER TABLE `py_rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `py_slides`
--
ALTER TABLE `py_slides`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `py_userse`
--
ALTER TABLE `py_userse`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
