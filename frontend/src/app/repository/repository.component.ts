import { Component, OnInit, Input } from '@angular/core';
import * as moment from 'moment';

@Component({
  selector: 'repository',
  templateUrl: './repository.component.html',
  styleUrls: ['./repository.component.scss']
})
export class RepositoryComponent implements OnInit {
  @Input() repo;
  @Input() number;
  constructor() { }

  ngOnInit() {
    this.repo.last_pushed_date = moment(this.repo.last_pushed_date, "YYYYMMDD").fromNow();
    this.repo.created_date = moment(this.repo.created_date).format('LL');
  }

}
