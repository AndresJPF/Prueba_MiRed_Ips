export interface User {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'empleado';
  created_at: string;
}

export interface UserCreate {
  name: string;
  email: string;
  password: string;
  role?: 'admin' | 'empleado';
}

export interface UserUpdate {
  name?: string;
  email?: string;
  password?: string;
  role?: 'admin' | 'empleado';
}

export interface UserListResponse {
  data: User[];
  total: number;
  page: number;
  page_size: number;
}
