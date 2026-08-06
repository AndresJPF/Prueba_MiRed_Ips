-- =====================================================
-- SEEDERS PARA MiRed IPS
-- Fecha: 2026-08-06
-- Descripción: Datos de prueba para usuarios, categorías y productos
-- =====================================================

USE mired_ips;

-- =====================================================
-- 1. LIMPIAR DATOS EXISTENTES (OPCIONAL)
-- =====================================================
-- Descomentar si quieres limpiar los datos antes de insertar
-- SET FOREIGN_KEY_CHECKS = 0;
-- TRUNCATE TABLE productos;
-- TRUNCATE TABLE categorias;
-- TRUNCATE TABLE users;
-- SET FOREIGN_KEY_CHECKS = 1;

-- =====================================================
-- 2. USUARIOS (users)
-- =====================================================

-- Administradores
INSERT INTO users (name, email, password, role, created_at) VALUES
('Administrador Principal', 'admin@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin', NOW()),
('Carlos Rodríguez', 'carlos.rodriguez@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin', NOW());

-- Empleados
INSERT INTO users (name, email, password, role, created_at) VALUES
('María González', 'maria.gonzalez@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'empleado', NOW()),
('Juan Pérez', 'juan.perez@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'empleado', NOW()),
('Ana Martínez', 'ana.martinez@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'empleado', NOW()),
('Luis Fernández', 'luis.fernandez@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'empleado', NOW()),
('Laura Sánchez', 'laura.sanchez@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'empleado', NOW());

-- Usuario con soft delete (eliminado lógicamente)
INSERT INTO users (name, email, password, role, created_at, deleted_at) VALUES
('Usuario Eliminado', 'eliminado@miredips.com', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'empleado', DATE_SUB(NOW(), INTERVAL 30 DAY), DATE_SUB(NOW(), INTERVAL 5 DAY));

-- =====================================================
-- 3. CATEGORÍAS (categorias)
-- =====================================================

INSERT INTO categorias (nombre, descripcion, created_at) VALUES
('Medicamentos', 'Productos farmacéuticos para tratamiento de enfermedades', NOW()),
('Equipos Médicos', 'Equipos y dispositivos médicos para diagnóstico y tratamiento', NOW()),
('Material de Curación', 'Insumos para curaciones y procedimientos menores', NOW()),
('Laboratorio', 'Reactivos y materiales para análisis clínicos', NOW()),
('Hospitalarios', 'Insumos generales para hospitalización y clínicas', NOW()),
('Cuidado Personal', 'Productos de higiene y cuidado personal', NOW()),
('Nutrición', 'Suplementos nutricionales y alimentos especializados', NOW()),
('Odontología', 'Insumos y equipos para procedimientos odontológicos', NOW()),
('Veterinaria', 'Productos para atención veterinaria', NOW()),
('Instrumental Quirúrgico', 'Instrumentos para procedimientos quirúrgicos', NOW());

-- =====================================================
-- 4. PRODUCTOS (productos)
-- =====================================================

-- Categoría: Medicamentos (id: 1)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('MED-001', 'Acetaminofén 500mg x 30 comp', 1, 'Analgésico y antipirético de uso común', 8500.00, 250, 'activo', NOW()),
('MED-002', 'Amoxicilina 500mg x 20 cáps', 1, 'Antibiótico de amplio espectro', 12500.00, 180, 'activo', NOW()),
('MED-003', 'Ibuprofeno 600mg x 20 comp', 1, 'Antiinflamatorio no esteroideo', 9800.00, 200, 'activo', NOW()),
('MED-004', 'Loratadina 10mg x 10 comp', 1, 'Antihistamínico para alergias', 7200.00, 150, 'activo', NOW()),
('MED-005', 'Omeprazol 20mg x 14 cáps', 1, 'Inhibidor de bomba de protones', 6500.00, 300, 'activo', NOW()),
('MED-006', 'Metformina 850mg x 30 comp', 1, 'Antidiabético oral', 11200.00, 120, 'activo', NOW()),
('MED-007', 'Losartán 50mg x 30 comp', 1, 'Antihipertensivo', 14300.00, 90, 'inactivo', NOW()),
('MED-008', 'Atorvastatina 20mg x 20 comp', 1, 'Reductor de colesterol', 18600.00, 160, 'activo', NOW());

-- Categoría: Equipos Médicos (id: 2)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('EQU-001', 'Estetoscopio Profesional', 2, 'Estetoscopio de doble campana para auscultación', 285000.00, 45, 'activo', NOW()),
('EQU-002', 'Esfigmomanómetro Digital', 2, 'Tensiómetro digital de brazo con pantalla LCD', 320000.00, 30, 'activo', NOW()),
('EQU-003', 'Glucometro Digital', 2, 'Medidor de glucosa en sangre con tiras reactivas', 180000.00, 25, 'activo', NOW()),
('EQU-004', 'Oximetro de Pulso', 2, 'Oxímetro de dedo para medición de saturación de oxígeno', 95000.00, 60, 'activo', NOW()),
('EQU-005', 'Termómetro Digital Infrarrojo', 2, 'Termómetro sin contacto para frente', 145000.00, 40, 'activo', NOW()),
('EQU-006', 'Nebulizador Ultrasónico', 2, 'Nebulizador portátil para tratamientos respiratorios', 420000.00, 15, 'inactivo', NOW());

-- Categoría: Material de Curación (id: 3)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('CUR-001', 'Gasas Estériles x 10 und', 3, 'Gasas de algodón estériles para curación', 6500.00, 500, 'activo', NOW()),
('CUR-002', 'Venda Elástica de 5cm x 5m', 3, 'Venda elástica adhesiva para compresión', 8500.00, 300, 'activo', NOW()),
('CUR-003', 'Apósitos Adhesivos Varios Tamaños', 3, 'Apósitos para heridas en diversos tamaños', 12500.00, 200, 'activo', NOW()),
('CUR-004', 'Venda de Gasas de 10cm x 10m', 3, 'Venda de gasa para inmovilización', 7500.00, 180, 'activo', NOW()),
('CUR-005', 'Cinta Micropore 2.5cm x 10m', 3, 'Cinta adhesiva hipoalergénica para fijación', 9800.00, 250, 'activo', NOW()),
('CUR-006', 'Esparadrapo de 5cm x 5m', 3, 'Esparadrapo para fijación de vendajes', 6700.00, 150, 'inactivo', NOW());

-- Categoría: Laboratorio (id: 4)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('LAB-001', 'Tubos de Ensayo x 50 und', 4, 'Tubos de ensayo de vidrio de 15ml', 28000.00, 80, 'activo', NOW()),
('LAB-002', 'Pipetas Desechables x 100 und', 4, 'Pipetas de plástico estériles de 3ml', 18500.00, 120, 'activo', NOW()),
('LAB-003', 'Reactivo de Hematología', 4, 'Reactivo para análisis de sangre completo', 45000.00, 40, 'activo', NOW()),
('LAB-004', 'Reactivo de Química Sanguínea', 4, 'Reactivo para perfil bioquímico', 52000.00, 35, 'activo', NOW());

-- Categoría: Hospitalarios (id: 5)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('HOS-001', 'Guantes de Látex x 100 und', 5, 'Guantes de látex quirúrgicos estériles', 35000.00, 400, 'activo', NOW()),
('HOS-002', 'Bata Desechable', 5, 'Bata quirúrgica desechable de polipropileno', 28000.00, 150, 'activo', NOW()),
('HOS-003', 'Gorro Quirúrgico x 100 und', 5, 'Gorros desechables para área quirúrgica', 15000.00, 200, 'activo', NOW()),
('HOS-004', 'Mascarilla Quirúrgica x 50 und', 5, 'Mascarillas desechables de 3 capas', 22000.00, 500, 'activo', NOW()),
('HOS-005', 'Guantes de Nitrilo x 100 und', 5, 'Guantes de nitrilo libres de látex', 42000.00, 180, 'inactivo', NOW());

-- Categoría: Cuidado Personal (id: 6)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('PER-001', 'Jabón Antibacterial x 500ml', 6, 'Jabón líquido antibacterial con clorhexidina', 18500.00, 200, 'activo', NOW()),
('PER-002', 'Crema Hidratante x 250g', 6, 'Crema hidratante para manos y cuerpo', 15500.00, 160, 'activo', NOW()),
('PER-003', 'Shampoo Medicado', 6, 'Shampoo con ketoconazol para caspa', 22500.00, 100, 'activo', NOW()),
('PER-004', 'Protector Solar FPS 50', 6, 'Bloqueador solar de amplio espectro', 38000.00, 80, 'inactivo', NOW());

-- Categoría: Nutrición (id: 7)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('NUT-001', 'Multivitamínico Completo x 30', 7, 'Suplemento vitamínico y mineral', 45000.00, 120, 'activo', NOW()),
('NUT-002', 'Proteína de Suero x 1kg', 7, 'Proteína en polvo para nutrición deportiva', 85000.00, 50, 'activo', NOW()),
('NUT-003', 'Glucosamina 1500mg x 30', 7, 'Suplemento para articulaciones', 55000.00, 70, 'activo', NOW()),
('NUT-004', 'Omegas 3 x 60 cáps', 7, 'Ácidos grasos esenciales omega 3', 62000.00, 90, 'inactivo', NOW());

-- Categoría: Odontología (id: 8)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('ODO-001', 'Gasas Dentales x 50 und', 8, 'Gasas estériles para procedimientos dentales', 18500.00, 120, 'activo', NOW()),
('ODO-002', 'Anestesia Dental', 8, 'Anestesia local para procedimientos dentales', 32000.00, 60, 'activo', NOW()),
('ODO-003', 'Implante Dental Standard', 8, 'Implante dental de titanio', 850000.00, 30, 'activo', NOW()),
('ODO-004', 'Sellante Dental', 8, 'Sellante para prevención de caries', 42000.00, 45, 'inactivo', NOW());

-- Categoría: Veterinaria (id: 9)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('VET-001', 'Antipulga para Perros', 9, 'Tratamiento antipulgas y garrapatas', 55000.00, 80, 'activo', NOW()),
('VET-002', 'Vacuna Antirrábica', 9, 'Vacuna para prevención de rabia', 35000.00, 60, 'activo', NOW()),
('VET-003', 'Desparasitante Canino', 9, 'Desparasitante interno y externo', 28000.00, 100, 'activo', NOW()),
('VET-004', 'Alimento Hipoalergénico x 10kg', 9, 'Alimento para mascotas con alergias', 120000.00, 30, 'inactivo', NOW());

-- Categoría: Instrumental Quirúrgico (id: 10)
INSERT INTO productos (codigo, nombre, categoria_id, descripcion, precio, stock, estado, created_at) VALUES
('INS-001', 'Bisturí Desechable Nº 10', 10, 'Hoja de bisturí desechable estéril', 8500.00, 200, 'activo', NOW()),
('INS-002', 'Pinzas Hemostáticas', 10, 'Pinzas hemostáticas de 14cm', 85000.00, 45, 'activo', NOW()),
('INS-003', 'Tijeras Quirúrgicas', 10, 'Tijeras quirúrgicas rectas de 15cm', 125000.00, 30, 'activo', NOW()),
('INS-004', 'Portaagujas', 10, 'Portaagujas quirúrgico de 18cm', 95000.00, 25, 'inactivo', NOW());

-- =====================================================
-- 5. VERIFICACIÓN DE DATOS
-- =====================================================

-- Mostrar conteo de registros
SELECT 'USUARIOS' as Tabla, COUNT(*) as Total FROM users
UNION ALL
SELECT 'CATEGORÍAS', COUNT(*) FROM categorias
UNION ALL
SELECT 'PRODUCTOS', COUNT(*) FROM productos;

-- Mostrar resumen de productos por categoría
SELECT 
    c.nombre AS Categoría,
    COUNT(p.id) AS Total_Productos,
    SUM(CASE WHEN p.estado = 'activo' THEN 1 ELSE 0 END) AS Activos,
    SUM(CASE WHEN p.estado = 'inactivo' THEN 1 ELSE 0 END) AS Inactivos
FROM categorias c
LEFT JOIN productos p ON c.id = p.categoria_id AND p.deleted_at IS NULL
GROUP BY c.id, c.nombre
ORDER BY c.nombre;

-- Mostrar usuarios por rol
SELECT 
    role AS Rol,
    COUNT(*) AS Total,
    SUM(CASE WHEN deleted_at IS NULL THEN 1 ELSE 0 END) AS Activos,
    SUM(CASE WHEN deleted_at IS NOT NULL THEN 1 ELSE 0 END) AS Eliminados
FROM users
GROUP BY role;

-- =====================================================
-- 6. DATOS DE PRUEBA PARA AUTENTICACIÓN
-- =====================================================

-- La contraseña para todos los usuarios es: "password123"
-- La contraseña hash corresponde a: $2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi
-- Puedes usar estas credenciales para pruebas:

-- Admin: admin@miredips.com / password123
-- Empleado: maria.gonzalez@miredips.com / password123

-- =====================================================
-- FIN DEL SCRIPT
-- =====================================================