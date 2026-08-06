import { Component, OnInit } from '@angular/core';
import { User } from '../../../../core/models/user.model';
import { UserService } from '../../../../core/services/user.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css'],
})
export class UserListComponent implements OnInit {
  users: User[] = [];
  loading = false;
  error = '';
  currentPage = 1;
  pageSize = 10;
  total = 0;

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.loadUsers();
  }

  loadUsers(): void {
    this.loading = true;
    this.error = '';
    this.userService.getUsers(this.currentPage, this.pageSize).subscribe({
      next: (response) => {
        this.users = response.data;
        this.total = response.total;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar los usuarios';
        this.loading = false;
        console.error(err);
      },
    });
  }

  deleteUser(id: number): void {
    if (!confirm('¿Estás seguro de eliminar este usuario?')) return;
    this.userService.deleteUser(id).subscribe({
      next: () => {
        this.loadUsers();
      },
      error: (err) => {
        this.error = 'Error al eliminar el usuario';
        console.error(err);
      },
    });
  }

  onPageChange(page: number): void {
    this.currentPage = page;
    this.loadUsers();
  }
}


