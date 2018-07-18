import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import {
  trigger,
  state,
  style,
  animate,
  transition
} from '@angular/animations';

import { DataService } from './services/data.service';

@Component({
  selector: 'app',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  animations: [
    trigger('loaderState', [
      state('active', style({
        display: 'none',
        opacity: 0
      })),
      state('inactive', style({
        display: 'block',
        opacity: 1
      })),
      transition('inactive => active', animate('300ms ease-in')),
      transition('active => inactive', animate('300ms ease-out'))
    ])
  ]
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  repositories: Repository[];
  total: number = 0;
  current: number = 1;
  totalPages: number = 1;
  private pages: number[] = [];
  private repoSubscription;
  private routeSubscription;
  private isLoaded: string = 'inactive';

  constructor(private dataService: DataService, private route: ActivatedRoute, private router: Router) {}

  ngOnInit() {
    this.routeSubscription = this.route.queryParams.subscribe(map => {
      this.current = map.page ? parseInt(map.page) : 1;
      this.repoSubscription = this.dataService.getRepositories(this.current).subscribe(repositories => {
        this.repositories = repositories['results'];
        this.total = repositories['count'];
        this.totalPages = (this.total % this.repositories.length) > 0 ? Math.floor(this.total / this.repositories.length) + 1 : this.total / this.repositories.length;
        for(let i = 0; i < this.totalPages; i++) {
          this.pages.push(i + 1);
        }
        this.isLoaded = 'active';
      }, error => {
        this.router.navigate(['/']);
      });
    });
  }

  navigate(page: number) {
    if(page <= 0 || page > this.totalPages) {
      return false;
    }
    this.router.navigate(['/'], { queryParams: { page: page }, queryParamsHandling: 'merge' });
    this.isLoaded = 'inactive';
  }

  ngOnDestroy() {
    this.repoSubscription.unsubscribe();
    this.routeSubscription.unsubscribe();
  }
}

export interface Repository {
  repositoryId: number;
  name: string;
  description: string;
  stars: number;
  url: string;
  createdDate: string;
  lastPushedDate: string;
}