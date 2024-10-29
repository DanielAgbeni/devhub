import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { SidebarLeft } from '@/components/Sidebar/Sidebar'
import ShowPosts from "@/components/Posts/ShowPosts"

const Feed = () => {
  return (
    <SidebarProvider>
      <SidebarLeft />
      <SidebarInset>
        <header className="sticky top-0 flex h-14 shrink-0 items-center gap-2 bg-background">
          <div className="flex flex-1 items-center gap-2 px-3">
            <SidebarTrigger />
          </div>
        </header>
        <main className="flex flex-col flex-grow overflow-hidden">
          <div className=" h-full">
            <ShowPosts />
          </div>
        </main>
      </SidebarInset>
    </SidebarProvider>
  )
}

export default Feed;
