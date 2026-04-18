-- SRWS PostgreSQL Schema (Auth YOK, 5 Kategori)
-- Kategoriler: Plastic | Paper & Cardboard | Metal | Battery | Glass

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE waste_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    color_hex VARCHAR(7) NOT NULL,
    icon_name VARCHAR(100) NOT NULL,
    recycling_bin_color VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE scan_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    device_id VARCHAR(255),
    category_name VARCHAR(100) NOT NULL,
    confidence_score DECIMAL(5,4) NOT NULL
        CHECK (confidence_score >= 0 AND confidence_score <= 1),
    ai_description TEXT,
    scanned_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

INSERT INTO waste_categories (name, color_hex, icon_name, recycling_bin_color, description) VALUES
('Plastic',           '#FFC107', 'local_drink',  'Yellow bin', 'Plastic bottles, bags, containers'),
('Paper & Cardboard', '#2196F3', 'description',  'Blue bin',   'Newspapers, cardboard boxes, office paper'),
('Metal',             '#9E9E9E', 'inbox',         'Grey bin',   'Cans, foil, metal containers'),
('Battery',           '#F44336', 'battery_alert', 'Red bin',    'AA, AAA, lithium, phone batteries'),
('Glass',             '#00BCD4', 'wine_bar',      'Blue bin',   'Glass bottles, jars');

CREATE INDEX idx_scan_history_device_id  ON scan_history(device_id);
CREATE INDEX idx_scan_history_scanned_at ON scan_history(scanned_at DESC);
