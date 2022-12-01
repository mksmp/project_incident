-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: std-mysql
-- Время создания: Дек 01 2022 г., 08:22
-- Версия сервера: 5.7.26-0ubuntu0.16.04.1
-- Версия PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `project_incident_db`
--
CREATE DATABASE IF NOT EXISTS `project_incident_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `project_incident_db`;

-- --------------------------------------------------------

--
-- Структура таблицы `accidents`
--

CREATE TABLE `accidents` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `accidents`
--

INSERT INTO `accidents` (`id`, `name`, `description`, `date`, `type_id`) VALUES
(1, 'Убийство на ул.Совесткая', 'Убийство совершено в подвале дома по адресу ул.Советская, д.1', '2022-11-20', 1),
(2, 'Наезд на пешехода ул.Декабристов', 'Наезд на пешехода ул.Декабристов, переходившего улицу в неположенном месте', '2022-11-21', 3),
(8, '123', '123', '2022-11-01', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `accidents_members`
--

CREATE TABLE `accidents_members` (
  `accidents_id` int(11) NOT NULL,
  `members_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Members`
--

CREATE TABLE `Members` (
  `id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `initials` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Members`
--

INSERT INTO `Members` (`id`, `first_name`, `initials`) VALUES
(1, 'Иванов', 'А.А.'),
(2, 'Петров', 'Б.Б.'),
(3, 'Сидоров', 'В.В.'),
(6, 'Петров', 'А.Б.'),
(7, '123', '33');

-- --------------------------------------------------------

--
-- Структура таблицы `types`
--

CREATE TABLE `types` (
  `id` int(11) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `types`
--

INSERT INTO `types` (`id`, `type`) VALUES
(1, 'Убийство'),
(2, 'Ограбление'),
(3, 'ДТП');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `accidents`
--
ALTER TABLE `accidents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `type_id` (`type_id`);

--
-- Индексы таблицы `accidents_members`
--
ALTER TABLE `accidents_members`
  ADD PRIMARY KEY (`accidents_id`,`members_id`),
  ADD KEY `members_id` (`members_id`);

--
-- Индексы таблицы `Members`
--
ALTER TABLE `Members`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `accidents`
--
ALTER TABLE `accidents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `Members`
--
ALTER TABLE `Members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `types`
--
ALTER TABLE `types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `accidents`
--
ALTER TABLE `accidents`
  ADD CONSTRAINT `accidents_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `accidents_members`
--
ALTER TABLE `accidents_members`
  ADD CONSTRAINT `accidents_members_ibfk_1` FOREIGN KEY (`accidents_id`) REFERENCES `Members` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `accidents_members_ibfk_2` FOREIGN KEY (`members_id`) REFERENCES `accidents` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
