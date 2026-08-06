import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../../../core/services/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})
export class NavbarComponent {
  constructor(
    private authService: AuthService,
    private router: Router,
  ) {}

  logout(): void {
    this.authService.logout().subscribe({
      next: () => {
        this.authService.removeToken();
        this.router.navigate(['/auth/login']);
      },
      error: () => {
        this.authService.removeToken();
        this.router.navigate(['/auth/login']);
      },
    });
  }
}
