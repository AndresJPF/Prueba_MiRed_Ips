import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from './components/navbar/navbar.component';
import { PaginationComponent } from './components/pagination/pagination.component';
import { LoadingSpinnerComponent } from './components/loading-spinner/loading-spinner.component';

@NgModule({
  declarations: [NavbarComponent, PaginationComponent, LoadingSpinnerComponent],
  imports: [CommonModule, RouterModule],
  exports: [NavbarComponent, PaginationComponent, LoadingSpinnerComponent],
})
export class SharedModule {}
