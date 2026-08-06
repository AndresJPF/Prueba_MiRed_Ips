export interface Product {
  id: number;
  codigo: string;
  nombre: string;
  categoria_id: number;
  descripcion: string | null;
  precio: number;
  stock: number;
  estado: 'activo' | 'inactivo';
}

export interface ProductCreate {
  codigo: string;
  nombre: string;
  categoria_id: number;
  descripcion?: string | null;
  precio: number;
  stock?: number;
  estado?: 'activo' | 'inactivo';
}

export interface ProductUpdate {
  codigo?: string;
  nombre?: string;
  categoria_id?: number;
  descripcion?: string | null;
  precio?: number;
  stock?: number;
  estado?: 'activo' | 'inactivo';
}

export interface ProductListResponse {
  data: Product[];
  total: number;
  page: number;
  page_size: number;
}
