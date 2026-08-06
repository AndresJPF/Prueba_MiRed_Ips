import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from '../../../../core/models/user.model';
import { UserService } from '../../../../core/services/user.service';

@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.css'],
})
export class UserDetailComponent implements OnInit {
  user: User | null = null;
  loading = false;
  error = '';

  constructor(
    private userService: UserService,
    private route: ActivatedRoute,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      if (params['id']) {
        this.loadUser(params['id']);
      }
    });
  }

  loadUser(id: number): void {
    this.loading = true;
    this.error = '';
    this.userService.getUser(id).subscribe({
      next: (user) => {
        this.user = user;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar el usuario';
        this.loading = false;
        console.error(err);
      },
    });
  }

  deleteUser(): void {
    if (!this.user) return;
    if (!confirm('¿Estás seguro de eliminar este usuario?')) return;

    this.userService.deleteUser(this.user.id).subscribe({
      next: () => {
        this.router.navigate(['/users']);
      },
      error: (err) => {
        this.error = 'Error al eliminar el usuario';
        console.error(err);
      },
    });
  }
}

